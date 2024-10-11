from src.fashion_recommendation_system.utils.data_utils import unzip_file
import logging

logging.basicConfig(level=logging.INFO)

def main():
    # Path to your zipped dataset file
    zip_file_path = 'data/raw/fashion_mnist.zip'
    extract_to_dir = 'data/processed/'

    # Unzipping the dataset
    unzip_file(zip_file_path, extract_to_dir)

if __name__ == "__main__":
    main()
