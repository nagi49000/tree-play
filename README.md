# tree-play
Repo for some simple experiments of tree-based ML algos.

Example data and problem description taken from
https://towardsdatascience.com/random-forest-in-python-24d0893d51c0

The repo contains an environment.yml for a conda environment, in which the notebooks can be run.

- data-analysis.ipynb looks at the raw data, and covers preliminaries for model fitting
- decision-tree.ipynb looks at the simplest form of model fitting of a decision tree, and some hyper parameter tuning
- random-forest.ipynb looks at improving on using a decision tree, and using SHAP to investigate the feature space
- boosted-trees.ipynb looks at improving on random forests, using boosted trees and grid search
