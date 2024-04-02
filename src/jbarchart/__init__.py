# import importlib.metadata
# import pathlib

# import anywidget
# import traitlets

# try:
#     __version__ = importlib.metadata.version("jbarchart")
# except importlib.metadata.PackageNotFoundError:
#     __version__ = "unknown"


# class Counter(anywidget.AnyWidget):
#     _esm = pathlib.Path(__file__).parent / "static" / "widget.js"
#     _css = pathlib.Path(__file__).parent / "static" / "widget.css"
#     value = traitlets.Int(0).tag(sync=True)


import importlib.metadata
import pathlib
from io import StringIO

import anywidget
import traitlets

try:
    __version__ = importlib.metadata.version("jbarchart")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"

class BarChart(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "static" / "widget.js"
    _css = pathlib.Path(__file__).parent / "static" / "widget.css"
    data = traitlets.Unicode().tag(sync=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def update(self, data):
        output = StringIO()
        data.to_csv(output, index=False)
        self.data = output.getvalue()
        output.close()
        return self

