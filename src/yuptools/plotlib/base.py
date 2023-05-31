from typing import Iterable, List, Tuple

from matplotlib.cm import ScalarMappable
import matplotlib.pyplot as plt
import torch

__all__ = [
    "BasePlot",
]


class BasePlot:
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
    ) -> None:
        self.figsize = figsize
        self.fontsize = fontsize

        # x-axis
        self.xlabel = xlabel
        self.xlim = xlim
        self.xticks = xticks
        self.xticklabels = xticklabels

        # y-axis
        self.ylabel = ylabel
        self.ylim = ylim
        self.yticks = yticks
        self.yticklabels = yticklabels

        # colorbar
        self.clabel = clabel
        self.cmap = plt.cm.get_cmap(cmap)
        self.clim = clim
        self.cticks = cticks
        self.cticklabels = cticklabels

        self.grid_alpha = grid_alpha

        self.fig, self.ax = None, None

    def pre_settings(
            self,
    ) -> None:
        plt.rcParams.update({
            "font.size": self.fontsize,
        })

        self.fig, self.ax = plt.subplots(
            figsize=self.figsize,
            nrows=1,
            ncols=1,
        )

    def post_settings(
            self,
    ) -> None:
        # x-axis
        self.ax.set_xlabel(self.xlabel)

        x_min, x_max = self.xlim
        self.ax.set_xlim(x_min, x_max)

        if self.xticks is not None:
            self.ax.set_xticks(
                ticks=self.xticks,
                labels=self.xticklabels,
            )

        # y-axis
        self.ax.set_ylabel(self.ylabel)

        y_min, y_max = self.ylim
        self.ax.set_ylim(y_min, y_max)

        if self.yticks is not None:
            self.ax.set_yticks(
                ticks=self.yticks,
                labels=self.yticklabels,
            )

        # grid
        self.ax.grid(alpha=self.grid_alpha)

    def color_settings(
            self,
    ) -> None:
        assert self.ax is not None

        c_min, c_max = self.clim

        cbar = ScalarMappable(
            norm=plt.Normalize(c_min, c_max),
            cmap=self.cmap,
        )
        cbar.set_array([])

        cbar = self.fig.colorbar(
            cbar,
            ax=self.ax,
            ticks=self.cticks,
        )

        cbar.ax.set_ylabel(self.clabel)

        if self.cticklabels is not None:
            cbar.ax.set_yticklabels(self.cticklabels)

    def draw_identity_line(
            self,
    ) -> None:
        assert self.ax is not None

        _range = [
            torch.iinfo(torch.int).min,
            torch.iinfo(torch.int).max,
        ]

        self.ax.plot(
            _range, _range,
            linestyle="dashed",
            linewidth=1,
            c="black",
        )

    def save(
            self,
            save_dir: str,
            save_name: str,
            fexts: List[str],
    ) -> None:
        from ..tools.pathtools import mkdir, join_path

        for fext in fexts:
            mkdir(join_path([save_dir, fext, ]))
            plt.savefig(
                join_path([
                    save_dir, fext,
                    f"{save_name}.{fext}",
                ]),
                dpi=300,
                bbox_inches="tight",
                pad_inches=0.05,
            )
        plt.draw()
        plt.close("all")

    def show(
            self,
    ) -> None:
        plt.show()
