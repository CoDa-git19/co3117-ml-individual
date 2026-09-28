# No reference implementation consulted at this point.
# Date: 2026-09-28

import numpy as np

def entropy(s):
    _, c = np.unique(s, return_counts=True)
    #Calculate probabilities
    p = c / c.sum()
    return -np.sum(p * np.log2(p))
    
def gini(s):
    _, c = np.unique(s, return_counts=True)
    p = c / c.sum()
    return 1.0 - np.sum(p ** 2)

def information_gain(parent, mask, criterion=entropy):
    # A branch is pure if all the samples belong to the same class. In that case, the information gain is 0.
    if mask.sum() == 0 or (~mask).sum() == 0:
        return 0.0
    n = len(parent)
    left_child = parent[mask]
    right_child = parent[~mask]
    w_left = len(left_child) / n
    w_right = len(right_child) / n
    return criterion(parent) - w_left * criterion(left_child) - w_right * criterion(right_child)

def best_split(X, y, criterion=entropy, n_thresholds=32):
    best_split_info = {
        "gain": 0.0,
        "feature": None,
        "threshold": None,
    }
    
    n_features = X.shape[1]
    for feature in range(n_features):
        feature_values = X[:, feature]
        # Skip the top and bottom 5% (outliers) to avoid creating extremely small leaf nodes
        percentiles = np.linspace(0.05, 0.95, n_thresholds)
        potential_thresholds = np.unique(np.quantile(feature_values, percentiles))

        # Evaluate each potential threshold
        for threshold in potential_thresholds:
            # Create a boolean mask: True for the Left child (<= threshold)
            left_mask = (feature_values <= threshold)
            # Calculate information gain
            current_gain = information_gain(y, left_mask, criterion=criterion)
        
            if current_gain > best_split_info["gain"]:
                best_split_info = {
                    "gain": float(current_gain),
                    "feature": int(feature),
                    "threshold": float(threshold)
                }
    return best_split_info