# RecSys CarbonAtor : Predicting Carbon Footprint of Recommendation System Algorithms

### [Public repository link!](https://github.com/giuspillo/carbon_recsys_radar)

Repository for the paper RecSys CarbonAtor: Predicting Carbon Footprint of Recommendation System Algorithms.

The system monitors the emissions produced by a recommendation algorithm when applied to a specific dataset. It executes the model using either the default parameter settings or by conducting hyperparameter tuning through grid search. Additionally, it records the metrics and parameter configurations from each run.

**Recommendations models, datasets and metrics refers to [Recbole](https://recbole.io/) implementation.**

**Emission tracking has been performed with [CodeCarbon](https://mlco2.github.io/codecarbon/) library.**


## Requirements
* **Global requirements**: Python >= 3.7 (tested on 3.8.5 and 3.11.4)
* **System requirements**: see requirements.txt


## Scripts

1. `src/tuning_tracker.py` performs hyperparameter tuning on a specified algorithm and dataset (both provided as script arguments), through grid search.

**Example**
```python
$ python3 src/tuning_tracker.py --dataset=movielens_1m --model=ItemKNN
```
2. `src/default_tracker.py` tracks the emissions of a specified algorithm with default parameters on a given dataset, both provided as script arguments.

**Example**
```python
$ python3 src/default_tracker.py --dataset=movielens_1m --model=ItemKNN
```

3. `notebooks/model-building.ipynb` is used to train and test the regression models of the paper, and produce the graphs reported in the paper.

This notebook uses the **[scikit-learn](https://scikit-learn.org/stable/)** library to train different regression models (SVR, DecisionTree, RandomForest, AdaBoost), and test them by computing error metrics (MAE, RSME, MLSE) and classification metrics (accuracy, precision, recall, F1).
It needs the emission information produced by the scripts 1. and/or 2, then it gathers them, and save the resulting file in the `regressor_data` folder.

## Datasets

All the datasets can be found in the `recsys_data` folder, and they follow the structure required by [Recbole](https://recbole.io/atomic_files.html)

* `recsys_data/movielens_1m`: dataset in the movie domain; it comes with knowledge information.
* `recsys_data/ml-10m_50U10I`: dataset in the movie domain; it comes with knowledge information.
* `recsys_data/amazon_books_60core_kg`: dataset in the book domain; it comes with knowledge information.
* `recsys_data/LFM-1b_artist_20U50I`: dataset in the music domain; it comes with knowledge information.
* `recsys_data/mind`: dataset in the news domain; there is no available knowledge information
