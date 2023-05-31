# yuptools.plotlib.bar.BarPlot

Creates bar plots.

- [Properties](#properties)
- Methods
  - [call](#call)
  - [save](#save)
  - [show](#show)


---


```
BarPlot(
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
)
```

## Properties

- **figsize** (*tuple*):
Figure size *(width, height)*.

- **fontsize** (*int*):
Font size for axis labels and ticks (default: *15*).

- **xlabel** (*str*):
X-axis label.

- **xlim** (*tuple*):
X-axis limits *(min, max)*.

- **xticks** (*iterable*):
X-axis tick positions.

- **xticklabels** (*list*):
Labels for X-axis ticks.

- **ylabel** (*str*):
Y-axis label.

- **ylim** (*tuple*):
Y-axis limits *(min, max)*.

- **yticks** (*iterable*):
Y-axis tick positions.

- **yticklabels** (*list*):
Labels for Y-axis ticks.

- **cmap** (*str*):
Colormap for bar colors (default: *viridis*).

- **clabel** (*str*):
Colorbar label.

- **clim** (*tuple*):
Colorbar limits *(min, max)*.

- **cticks** (*iterable*):
Colorbar tick positions.

- **cticklabels** (*list*):
Labels for colorbar ticks.

- **grid_alpha** (*float*):
Alpha value for grid lines (default: *0.*).

- **draw_identity** (*bool*):
Whether to draw identity line (default: *False*).


## Methods


### *call*

Creates a bar plot.

- **x**:
X-values for the bars.

- **y**:
Y-values for the bars.

- **c** (*optional*):
Color values for the bars.

```
plot = BarPlot(...)
plot(
    x,
    y,
    c: Optional = None,
)
```


### save

Saves the plot to multiple file formats.

- **save_dir**:
Directory to save the plot.

- **save_name**:
Base name for the saved files.

- **fexts**:
List of file extensions to save the plot (e.g., *["png", "pdf"]*).

```
plot = BarPlot(...)
plot(x, y, c)
plot.save(
    save_dir: str,
    save_name: str,
    fexts: List[str],
)
# save_dir
# └ fext1
#   └ save_name.fext1
# 
# └ fext2
#   └ save_name.fext2
#  ...
```


### show

Displays the plot.

```
plot = BarPlot(...)
plot(x, y, c)
plot.show()
```
