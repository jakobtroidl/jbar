import importlib.metadata
import pathlib
from io import StringIO

import anywidget
import traitlets
import ipywidgets as widgets


try:
    __version__ = importlib.metadata.version("jbar")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"

class BarChart(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "static" / "widget.js"
    _css = pathlib.Path(__file__).parent / "static" / "widget.css"
    data = traitlets.Unicode().tag(sync=True)
    x = traitlets.Unicode().tag(sync=True)
    exclude = traitlets.List().tag(sync=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def update(self, data, x, exclude=[]):
        self.x = x
        self.exclude = exclude

        # remove unwanted columns
        if self.exclude:
            data.drop(self.exclude, axis=1, inplace=True)
        
        output = StringIO()
        data.to_csv(output, index=False)
        self.data = output.getvalue()
        output.close()
        
    
    def dropdown_change(self, change):
        print(change)
        
    def show(self):
        dropdown = widgets.Dropdown(
            options=[('One', 1), ('Two', 2), ('Three', 3)],
            value=2,
            description='Number:',
        )

        dropdown.observe(self.dropdown_change)

        plot = widgets.VBox(
            children=[self],
            layout=widgets.Layout(
                flex='1',
                width='auto'
            )
        )
        return widgets.VBox([dropdown, plot])
        

