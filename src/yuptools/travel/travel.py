from typing import Tuple

import torch
import tqdm

from .config import *

__all__ = [
    "Traveler",
]


class Traveler:
    def __init__(
            self,
            model: torch.nn.Module,
            method: str = default_method,
            perp: bool = False,
            normalize: str = default_normalize,
            bound: bool = False,
            seed: int = default_seed,
            use_cuda: bool = False,
            verbose: bool = False,
            init_eps: float = 1e-3,
            stride: float = 1e-3,
            stride_decay: float = 0.5,
            tol: float = 1e-10,
            max_iter: int = 10000,
            turnaround: float = 0.1,
    ) -> None:
        from .direction import DirectionGenerator

        assert stride > 0
        assert 0 < stride_decay < 1

        self.model = model

        # travel direction
        self.method = method
        self.perp = perp
        self.normalize = normalize
        self.seed = seed
        self.direction_generator = DirectionGenerator(
            model=model,
            method=method,
            perp=perp,
            normalize=normalize,
            seed=seed,
            use_cuda=use_cuda,
        )

        # travel hyperparameters
        self.bound = bound

        self.hyperparameters = {
            "init_eps": init_eps,
            "stride": stride,
            "stride_decay": stride_decay,
        }
        self.epsilon = init_eps
        self.stride = stride
        self.stride_decay = stride_decay
        self.tol = tol
        self.max_iter = max_iter
        self.turnaround = turnaround

        self.correct = None
        self._correct = None
        self.flag = False

        self.use_cuda = use_cuda
        self.machine = "cuda" if use_cuda else "cpu"
        self.verbose = verbose

        self.num_data = 0

        Traveler.__name__ = \
            f"{self.method}_travel(" \
            f"perp={self.perp}, " \
            f"normalize={self.normalize}, " \
            f"bound={self.bound}, " \
            f"seed={self.seed}" \
            f")"

    def __call__(
            self,
            data: torch.Tensor,
            targets: torch.Tensor,
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        self.num_data = len(data)

        directions = self.direction_generator(data, targets)

        traveled_data = torch.zeros_like(data)
        epsilons = torch.zeros(size=(self.num_data,))

        for i in range(self.num_data):
            traveled_data[i], epsilons[i] = self.travel(
                data=data[i],
                target=targets[i],
                direction=directions[i],
                i=i,
            )

            self.reset()

        return traveled_data, epsilons

    def reset(
            self,
    ) -> None:
        self.epsilon = self.hyperparameters["init_eps"]
        self.stride = self.hyperparameters["stride"]
        self.stride_decay = self.hyperparameters["stride_decay"]

        self.correct = None
        self._correct = None
        self.flag = False

    def update(
            self,
            iteration: int,
    ) -> None:
        # crossed the decision boundary
        if self.correct != self._correct:
            self.flag = True

            # decrease epsilon & stride
            self.epsilon = self.epsilon - self.stride
            self.stride = self.stride * self.stride_decay

        # still inside the decision region
        else:
            self.flag = False

            # increase epsilon
            self.epsilon = self.epsilon + self.stride

        # epsilon must be over 0
        if self.epsilon < 0:
            self.epsilon = 0

        # divergence test:
        # if data still remains inside its decision region (no change in stride)
        # after {turnaround * 100}% of max_iter,
        # end travel.
        if iteration > self.max_iter * self.turnaround \
                and self.stride == self.hyperparameters["stride"]:
            self.flag = "break"

    def is_correct(
            self,
            data: torch.Tensor,
            target: torch.Tensor,
    ) -> bool:
        output = self.model(data.detach().to(self.machine)).detach().to("cpu")

        conf = torch.nn.Softmax(dim=-1)(output)
        pred = torch.argmax(conf, dim=-1)

        return bool(torch.eq(pred, target))

    def travel(
            self,
            data: torch.Tensor,
            target: torch.Tensor,
            direction: torch.Tensor,
            i: int,
    ) -> Tuple[torch.Tensor, float]:
        data = data.unsqueeze(dim=0)

        self.correct = self.is_correct(data, target)

        if not self.correct:
            return data, eps_for_incorrect

        _data = data

        for iteration in tqdm.trange(
                self.max_iter,
                desc=f"[{i + 1}/{self.num_data}] {Traveler.__name__}",
                disable=not self.verbose,
        ):
            self._correct = self.correct

            _data = data + (direction * self.epsilon)

            if self.bound:
                _data = _data.clamp(0, 1)

            self.correct = self.is_correct(_data, target)

            # print(f"[eps: {self.epsilon}, stride: {self.stride}] {self._correct} -> {self.correct}")

            self.update(iteration)

            # diverged
            if self.flag == "break":
                return data, eps_for_divergence

            # converged: just crossed the decision boundary
            if self.stride < self.tol and not self.correct:
                return _data, self.epsilon

        # not fully converged
        return _data, -self.epsilon
