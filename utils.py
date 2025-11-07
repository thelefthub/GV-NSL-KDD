
import numpy as np
import matplotlib.pyplot as plt



def load_split(name: str, data_dir: str):

    X_path, y_path = data_dir / f"X_{name}.npy", data_dir / f"y_{name}.npy"
    if X_path.exists() and y_path.exists():
        X = np.load(X_path, allow_pickle=False)
        y = np.load(y_path, allow_pickle=False)
        return X, y
    # fallback: load from CSV if .npy not found
    X_path, y_path = data_dir / f"X_{name}.csv", data_dir / f"y_{name}.csv"
    X = np.loadtxt(X_path, delimiter=",", dtype=np.float32)
    y = np.loadtxt(y_path, delimiter=",")
    return X, y