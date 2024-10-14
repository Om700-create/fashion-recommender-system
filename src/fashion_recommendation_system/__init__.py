# src/fashion_recommendation_system/__init__.py
import logging
from fashion_recommendation_system.pipeline.pipeline import run_pipeline

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run_pipeline()
