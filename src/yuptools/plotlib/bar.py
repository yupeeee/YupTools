from typing import Iterable, List, Optional, Tuple

from .base import BasePlot

__all__ = [
    "BarPlot",
]


class BarPlot(BasePlot):
    def __init__(
            self,
            figsize: Tuple[float, float] = None,
            fontsize: float = 15,
            xlabel: str = None,
            xlim: Tuple[float, float] = (None, None),
            xticks: Iterable[float] = None,
            xticklabels: List[str] = None,
            ylabel: str = None,
            ylim: Tuple[float, float] = (None, None),
            yticks: Iterable[float] = None,
            yticklabels: List[str] = None,
            cmap: str = "viridis",
            clabel: str = None,
            clim: Tuple[float, float] = (None, None),
            cticks: Iterable[float] = None,
            cticklabels: List[str] = None,
            grid_alpha: float = 0.,
            draw_identity: bool = False,
    ) -> None:
        super().__init__(
            figsize=figsize,
            fontsize=fontsize,
            xlabel=xlabel,
            xlim=xlim,
            xticks=xticks,
            xticklabels=xticklabels,
            ylabel=ylabel,
            ylim=ylim,
            yticks=yticks,
            yticklabels=yticklabels,
            cmap=cmap,
            clabel=clabel,
            clim=clim,
            cticks=cticks,
            cticklabels=cticklabels,
            grid_alpha=grid_alpha,
        )

        self.draw_identity = draw_identity

    def __call__(
            self,
            x,
            y,
            c: Optional = None,
    ) -> None:
        self.pre_settings()

        color = self.cmap(c) if c is not None else None

        self.ax.bar(
            x, y,
            width=1 / len(x),
            color=color,
            edgecolor="black",
            linewidth=.5,
        )

        if c is not None:
            self.color_settings()

        if self.draw_identity:
            self.draw_identity_line()

        self.post_settings()
