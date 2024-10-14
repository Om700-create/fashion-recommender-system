import os
from pathlib import Path
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Project name
project_name = 'fashion_recommendation_system'

# List of files and directories to create
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/model_training.py",
    f"src/{project_name}/components/recommendation.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/pipeline.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "models/.gitkeep",  # Directory for saved models (RF, PCA, SVD)
    "data/fashion_mnist.csv",  # Dataset placeholder
    "templates/index.html",  # HTML template for UI
    "notebooks/EDA.ipynb",  # Notebook for Exploratory Data Analysis
    "notebooks/model_training.ipynb",  # Notebook for model training
    "notebooks/recommendation.ipynb",  # Notebook for recommendations
    "dvc.yaml",  # Data version control file
    "params.yaml",  # Parameters for experiments
    "requirements.txt",  # Dependencies
    "setup.py",  # Project setup script
    "data/raw/.gitkeep",  # For storing raw dataset files
    "data/processed/.gitkeep"  # For storing processed datasets
]

# Create directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directories
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create empty files
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
