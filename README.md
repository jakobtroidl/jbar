# jbar

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
