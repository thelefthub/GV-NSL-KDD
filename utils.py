
import numpy as np
import matplotlib.pyplot as plt

# Created using NSL-KDD documentation
COLUMNS = [
    "duration","protocol_type","service","flag","src_bytes","dst_bytes",
    "land","wrong_fragment","urgent","hot","num_failed_logins","logged_in",
    "num_compromised","root_shell","su_attempted","num_root","num_file_creations",
    "num_shells","num_access_files","num_outbound_cmds","is_host_login","is_guest_login",
    "count","srv_count","serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate",
    "same_srv_rate","diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count",
    "dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate",
    "dst_host_rerror_rate","dst_host_srv_rerror_rate","label","difficulty_level"
]

CATEGORICAL_COLS = ["protocol_type", "service", "flag"]

FEATURE_COLUMNS = [c for c in COLUMNS if c not in ["label", "difficulty_level"]]

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