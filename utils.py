
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

DOS = {
    "back","land","neptune","pod","smurf","teardrop",
    "mailbomb","apache2","processtable","udpstorm"
}
PROBE = {"satan","ipsweep","nmap","portsweep","mscan","saint", "worm"}
R2L = {
    "guess_passwd","ftp_write","imap","phf","multihop","warezmaster","warezclient",
    "spy","xlock","xsnoop","snmpguess","snmpgetattack","httptunnel","sendmail","named"
}
U2R = {"buffer_overflow","loadmodule","perl","rootkit","ps","sqlattack","xterm"}

def to_category(lbl: str) -> str:
    if lbl == "normal":
        return "normal"
    if lbl in DOS:
        return "dos"
    if lbl in PROBE:
        return "probe"
    if lbl in R2L:
        return "r2l"
    if lbl in U2R:
        return "u2r"
    raise ValueError(f"Unmapped attack label: {lbl}")

def load_split(name: str, data_dir):

    X_path = data_dir / f"X_{name}.npy"
    y_path = data_dir / f"y_{name}.npy"

    if not X_path.exists():
        raise FileNotFoundError(f"Missing feature file: {X_path}")
    if not y_path.exists():
        raise FileNotFoundError(f"Missing label file: {y_path}")

    X = np.load(X_path, allow_pickle=False)
    y = np.load(y_path, allow_pickle=False)
    return X, y

def make_binary_labels(y, normal_class_id):
    """
    Convert multi-class labels to binary:
      0 = normal class
      1 = any other class (intrusive)

    Args:
        y :    (array_like Shape (m,))
        normal_class_id : (int)             Encoded id of the 'normal' class
    
    Returns:
        y_bin : (array_like Shape (m,))     Binary labels (0 = normal, 1 = intrusive).
    """
    return (y != normal_class_id).astype(int)