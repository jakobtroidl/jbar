import importlib.metadata
import pathlib
from io import StringIO
import ipywidgets as widgets

import anywidget
import traitlets

try:
    __version__ = importlib.metadata.version("jbarchart")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"


class BarChart:
    def __init__(self, data):
        self.widget = Counter()
        self.update(data)

    def update(self, data):
        output = StringIO()
        data.to_csv(output, index=False)
        self.widget.data = output.getvalue()
        output.close()

    def show(self):
        return self.widget

class Counter(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "static" / "widget.js"
    _css = pathlib.Path(__file__).parent / "static" / "widget.css"
    data = traitlets.Unicode().tag(sync=True)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    # def show(self):
    #     # plots = widgets.VBox(
    #     #     children=[self],
    #     #     layout=widgets.Layout(
    #     #         flex='1',
    #     #         width='auto'
    #     #     )
    #     # )
    #     return self
