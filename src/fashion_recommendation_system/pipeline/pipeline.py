import logging
from fashion_recommendation_system.utils.common import load_dataset
from fashion_recommendation_system.components.model_training import train_model, evaluate_model, save_model
from fashion_recommendation_system.components.recommendation import apply_pca, apply_svd

def run_pipeline(config):
    # Load the data
    data = load_dataset(config['data_path'])

    # Prepare features and labels
    X = data.drop(columns=['label'])
    y = data['label']

    # Train the model
    rf_model = train_model(X, y)

    # Evaluate the model
    accuracy, report = evaluate_model(rf_model, X, y)

    # Save the trained model
    save_model(rf_model, config['model_save_path'])

    # Apply PCA and SVD
    pca, X_pca = apply_pca(X)
    svd, X_svd = apply_svd(X_pca)

    # Save PCA and SVD models
    save_model(pca, config['pca_model_save_path'])
    save_model(svd, config['svd_model_save_path'])

    return accuracy, report

