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
    _esm = pathlib.Path(__file__).parent / "widget.js"
    # _css = pathlib.Path(__file__).parent / "widget.css"
    data = traitlets.Unicode().tag(sync=True)
    x = traitlets.Unicode().tag(sync=True)
    exclude = traitlets.List().tag(sync=True)
    selection = traitlets.Int().tag(sync=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stacked_checkbox = widgets.Checkbox(
            value=False,
            description='Stacked',
            disabled=False,
            indent=True
        )
        self.stacked_checkbox.observe(self.stacked_change)

        
    def update(self, data, x, exclude=[]):
        self.x = x
        self.exclude = exclude
        self.selection = 0

        exclude_exists = all(column in data.columns for column in exclude)
        # remove unwanted columns
        if self.exclude and exclude_exists:
            data = data.drop(self.exclude, axis=1)
        
        # bring x to the front
        data = data[[x] + data.drop(columns=[x]).columns.tolist()]

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
            self.selection = change['new'] + 1
            self.send({"type": "update-selection", "value": self.selection})

    def stacked_change(self, change):
        if change['type'] == 'change' and change['name'] == 'value':
            # self.send({"type": "update-stacked", "value": change['new']})
            print("Hit Checkbox")
        
    def show(self):
        toolbar = widgets.HBox([self.dropdown, self.stacked_checkbox])
        plot = widgets.VBox(
            children=[self],
            layout=widgets.Layout(
                flex='1',
                width='auto'
            )
        )
        return widgets.VBox([toolbar, plot])
        

