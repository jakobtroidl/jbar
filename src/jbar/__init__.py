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
        
    
    def dropdown_change(self, change):
        if change['type'] == 'change' and change['name'] == 'value':
            print("changed to %s" % change['new'])
        
    def show(self):
        options = [(col, i) for i, col in enumerate(self.columns)]
        dropdown = widgets.Dropdown(
            options=options,
            value=0,
            description='Options:',
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
        

