from sklearn.decomposition import PCA, TruncatedSVD
import joblib

def apply_pca(X, n_components=50):
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X)
    return pca, X_pca

def apply_svd(X, n_components=50):
    svd = TruncatedSVD(n_components=n_components)
    X_svd = svd.fit_transform(X)
    return svd, X_svd

def save_model(model, filepath):
    joblib.dump(model, filepath)


