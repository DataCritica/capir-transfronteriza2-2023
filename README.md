# CAPIR Transfronteriza2 2023
Data analysis of anti-rights groups accounts on Twitter from Brazil, Ecuador, Colombia and Honduras.

Created by: Fer Aguirre

---
## Directory Structure
```
├── .gitignore
├── .gitsecret
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── assets
│   ├── brasil
│   │   ├── brasil.html
│   │   ├── brasil.txt
│   │   ├── brasil_centroids.png
│   │   └── brasil_clusters.png
│   ├── colombia
│   │   ├── colombia.html
│   │   ├── colombia.txt
│   │   ├── colombia_centroids.png
│   │   └── colombia_clusters.png
│   ├── ecuador
│   │   ├── ecuador.html
│   │   ├── ecuador.txt
│   │   ├── ecuador_centroids.png
│   │   └── ecuador_clusters.png
│   └── honduras
│       ├── honduras.html
│       ├── honduras.txt
│       ├── honduras_centroids.png
│       └── honduras_clusters.png
├── capir_transfronteriza2_2023
│   ├── __init__.py
│   ├── data
│   │   ├── __init__.py
│   │   ├── analyze.py
│   │   ├── export.py
│   │   ├── load.py
│   │   └── process.py
│   └── utils
│       ├── __init__.py
│       └── paths.py
├── data
│   ├── processed
│   └── raw
├── docs
│   ├── data-dictionary.md
│   └── references
├── notebooks
│   ├── 0.0-collect-tweets.ipynb
│   ├── 1.0-process-data.ipynb
│   ├── 2.0-analyze-data.ipynb
│   ├── 3.0-embeddings.ipynb
│   ├── 3.1-embeddings.ipynb
│   ├── 3.2-embeddings.ipynb
│   └── 3.3-embeddings.ipynb
├── outputs
│   ├── figures
│   └── tables
├── requirements.txt
├── scripts
└── setup.py
```
---

## License

This project is released under [MIT License](/LICENSE).

---

This repository was generated with [cookiecutter](https://github.com/cookiecutter/cookiecutter).