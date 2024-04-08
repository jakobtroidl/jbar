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
    selection = traitlets.Int().tag(sync=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def update(self, data, x, exclude=[]):
        self.x = x
        self.exclude = exclude
        self.selection = 0

        exclude_exists = all(column in data.columns for column in exclude)
        # remove unwanted columns
        if self.exclude and exclude_exists:
            data = data.drop(self.exclude, axis=1)

        self.columns = data.columns.tolist()
        self.columns.remove(x)
        
        output = StringIO()
        data.to_csv(output, index=False)
        self.data = output.getvalue()
        output.close()

        options = [(col, i) for i, col in enumerate(self.columns)]
        self.dropdown = widgets.Dropdown(
            options=options,
            value=0,
            description='Options:',
        )
        self.dropdown.observe(self.dropdown_change)
        
    
    def dropdown_change(self, change):
        if change['type'] == 'change' and change['name'] == 'value':
            self.selection = change['new']
            self.send({"type": "update-selection", "value": self.selection})
        
    def show(self):
        plot = widgets.VBox(
            children=[self],
            layout=widgets.Layout(
                flex='1',
                width='auto'
            )
        )
        return widgets.VBox([self.dropdown, plot])
        

