import os
import zipfile
import logging

def unzip_file(zip_file_path, extract_to_dir):
    """
    Unzips the given zip file into the target directory.

    Args:
        zip_file_path (str): The path to the zip file.
        extract_to_dir (str): The directory where the contents should be extracted.
    """
    if not os.path.exists(extract_to_dir):
        os.makedirs(extract_to_dir)
        logging.info(f"Created directory: {extract_to_dir}")

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_dir)
        logging.info(f"Extracted {zip_file_path} to {extract_to_dir}")