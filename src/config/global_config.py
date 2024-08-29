"""
The collection of global configurations
"""
CONFIG = {
	'DATASETS':				[
								'LFM-1b_artist_20U50I',
								'movielens_1m'
							],
	'MODELS':				
							['BPR', 'CFKG', 'CKE', 'DMF', 'KGCN', 'KGNNLS', 'LINE', 'MultiDAE', 'LightGCN', 'NGCF', 'DGCF']
,
	'LOG_FILE':				'log/carbon_tuning.log',
	'LOG_FILE_DEFAULT':		'log/carbon_default.log',
	'DATASET_PATH':			'data/',
	'RESULT_PATH':			'results/',
	'RESULT_PATH_SHARED':	'results_shared/',
	'RESULT_PATH_SHARED2':	'results_shared2/',
	'EMISSIONS_FILE':		'/emissions.csv',
	'METRICS_FILE':			'/metrics.csv',
	'PARAMS_FILE':			'/params.csv',
	'STATIC_CONFIG_FILE':	'src/config/_params.yaml',
	'HP_CONFIG_PATH':		'src/config/hyperparam/',
	'COUNTER':				1,
	'DATASETAZURE_FILE':	'notebooks/data/dataset_azure.csv',
	'DATASET_FILE':			'notebooks/data/dataset.csv'
}


def get_global_config():
	"""
	The getter method
	"""
	return CONFIG


def set_global_config(key, value):
	"""
	The setter method
	"""
	CONFIG.update({key: value})