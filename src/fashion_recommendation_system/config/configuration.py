import yaml
import logging

def load_config(path):
    try:
        with open(path, 'r') as file:
            config = yaml.safe_load(file)
        logging.info(f"Configuration loaded from {path}")
        return config
    except Exception as e:
        logging.error(f"Error loading config: {e}")
        raise

