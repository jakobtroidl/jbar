[![PyPI](https://img.shields.io/pypi/v/jbar.svg?color=green)](https://pypi.org/project/jbar/)
[![License](https://img.shields.io/pypi/l/anywidget.svg?color=green)](https://github.com/jakobtroidl/jbar/raw/main/LICENSE)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1OuASVyOI8LkeNk6ZLoRbL80kw6uwyd7P?usp=sharing)
  
## Interactive Jupyter Barchart
This is an interactive bar chart widget for Jupyter Notebook, VS Code, and Google Colab.
### Get started

```bash
pip install jbar
```

```python
import pandas as pd
from jbar import BarChart

df = pd.read_csv('https://raw.githubusercontent.com/jakobtroidl/jbarchart/master/data/test_features.csv')
barchart = BarChart()
barchart.update(df, x="cell_type", exclude=["id"])
barchart.show()
```
![demo_short](https://github.com/jakobtroidl/jbar/assets/29884213/fb8ecee8-5e44-41d4-bcb2-aee3defe9d28)

## Development installation

Create a virtual environment and install jbar in *editable* mode with the
optional development dependencies:

```sh
poetry install
poetry shell
```

You then need to install the JavaScript dependencies and run the development server.

```sh
npm install
npm run dev
```

Open `example.ipynb` in JupyterLab, VS Code, or your favorite editor
to start developing. Changes made in `js/` will be reflected
in the notebook.

## Publish to PyPI

```sh
// Update version in pyproject.toml
poetry build
poetry publish
```
