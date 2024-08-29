# RecSys Carbon Radar : Predicting Carbon Footprint of Recommendation System Algorithms

Repository for the paper RecSys Carbon Radar: Predicting Carbon Footprint of Recommendation System Algorithms.

The system monitors the emissions produced by a recommendation algorithm when applied to a specific dataset. It executes the model using either the default parameter settings or by conducting hyperparameter tuning through grid search. Additionally, it records the metrics and parameter configurations from each run.

**Recommendations models, datasets and metrics refers to [@Recbole](https://recbole.io/) implementation.**

**Emission tracking has been performed with [@CodeCarbon](https://mlco2.github.io/codecarbon/) library.**


## Requirements
* **Global requirements**: Python >= 3.7 (tested on 3.8.5 and 3.11.4)
* **System requirements**: see requirements.txt


## Scripts

1. src/tuning_tracker.py performs hyperparameter tuning on a specified algorithm and dataset (both provided as script arguments), through grid search.

NOTES:
- Available models and datasets are defined in the src/config/global_config.py file.
- Grid-search params values are defined in the src/config/hyperparam folder.
- Results are stored in the results folder.

**Example**
```python
$ python3 src/tuning_tracker.py --dataset=movielens_1m --model=ItemKNN
```
2. src/default_tracker.py tracks the emissions of a specified algorithm with default parameters on a given dataset, both provided as script arguments.

NOTES:
- Available models and datasets are defined in the src/config/global_config.py file.
- Feafult parameter values are definded in the src/config/params_config.py file.
- Results are store in the results_shared folder.

**Example**
```python
$ python3 src/default_tracker.py --dataset=movielens_1m --model=ItemKNN
```


3. notebooks/model-building.ipynb is used to train and test the regression models of the paper, and produce the graphs reported in the paper.

## Datasets

* data/movielens_1m: dataset in the movie domain; it comes with knowledge information.
* data/ml-10m_50U10I: dataset in the movie domain; it comes with knowledge information.
* data/amazon_books_60core_kg: dataset in the book domain; it comes with knowledge information.
* data/LFM-1b_artist_20U50I: dataset in the music domain; it comes with knowledge information.
* data/mind: dataset in the news domain; there is no available knowledge information


## Acknowledgments

- **[@Recbole](https://recbole.io/)**
- **[@CodeCarbon](https://mlco2.github.io/codecarbon/)**

## License

Distributed under the [MIT](https://choosealicense.com/licenses/mit/) License. See `LICENSE.txt` for more information.