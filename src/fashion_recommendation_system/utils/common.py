import pandas as pd

def load_dataset(filepath):
    return pd.read_csv(filepath)

def load_config(filepath):
    import yaml
    with open(filepath, 'r') as file:
        config = yaml.safe_load(file)
    return config

