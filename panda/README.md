# Panda

Panda is a lightweight notebook-based data analysis workspace for exploring CSV datasets in Python.

The repository currently contains notebooks for data exploration and feature extraction, along with the source datasets used in those notebooks.

## Project Overview

This workspace is organized around interactive analysis in Jupyter notebooks. It is intended for:

- data exploration and cleanup
- notebook-driven experimentation
- feature extraction and analysis workflows
- reviewing structured CSV datasets

## Repository Structure

```text
.
├── anime.csv
├── Countries.csv
├── country.ipynb
├── FeatureExtraction.ipynb
├── panda.ipynb
├── kickbacks.vsix
└── .vscode/
```

## Notebooks

- `panda.ipynb` - main working notebook in the project.
- `country.ipynb` - notebook focused on country-related analysis.
- `FeatureExtraction.ipynb` - notebook for feature extraction experiments.

## Data Files

- `anime.csv` - dataset used for anime-related analysis.
- `Countries.csv` - dataset used for country-related analysis.

## Getting Started

1. Open the project folder in VS Code or Jupyter Notebook.
2. Launch the notebook you want to work with.
3. Run the cells in order from top to bottom.
4. Update the notebooks or datasets as needed for your analysis.

## Requirements

The repository does not currently include a dependency file such as `requirements.txt` or `environment.yml`.

Typical tools for working with this project include:

- Python 3
- Jupyter Notebook or VS Code notebooks
- `pandas`
- `numpy`
- `matplotlib` or `seaborn` if visualization is needed

## Notes

- This project is notebook-first and does not currently expose a packaged application or API.
- The VS Code extension package `kickbacks.vsix` is present in the workspace but is not required to run the notebooks.

## Suggested Next Steps

- Add a `requirements.txt` or `environment.yml`
- Document the purpose of each notebook in more detail
- Include example outputs or screenshots
- Add a short data dictionary for each CSV file
