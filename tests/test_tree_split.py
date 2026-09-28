import numpy as np
from src.from_scratch.tree_split import entropy, gini, information_gain, best_split


def test_entropy_known_values():
    # Perfectly balanced (50-50) -> Entropy = 1.0
    assert abs(entropy(np.array([0, 0, 1, 1])) - 1.0) < 1e-9
    # Pure node (100%) -> Entropy = 0.0
    assert abs(entropy(np.array([1, 1, 1, 1])) - 0.0) < 1e-9
    # Imbalanced 3:1 ratio
    exact_entropy = -(0.75 * np.log2(0.75) + 0.25 * np.log2(0.25))
    assert abs(entropy(np.array([0, 0, 0, 1])) - exact_entropy) < 1e-9

def test_gini_known_values():
    # Perfectly balanced
    assert abs(gini(np.array([0, 0, 1, 1])) - 0.5) < 1e-9
    # Pure node
    assert abs(gini(np.array([1, 1, 1, 1])) - 0.0) < 1e-9
    # Imbalanced 3:1 ratio
    assert abs(gini(np.array([0, 0, 0, 1])) - 0.375) < 1e-9

def test_information_gain_perfect_split():
    s = np.array([0, 0, 1, 1])
    # Perfect split: the left branch gets all 0s, the right branch gets all 1s
    mask = np.array([True, True, False, False]) 
    gain = information_gain(s, mask, criterion=entropy)
    # Parent entropy (1.0) - Children impurity (0.0) = 1.0
    assert abs(gain - 1.0) < 1e-9

def test_information_gain_empty_branch():
    s = np.array([0, 0, 1, 1])
    # All data goes to the left branch
    mask = np.array([True, True, True, True])
    gain = information_gain(s, mask, criterion=entropy)
    # The gain must be 0.0
    assert not np.isnan(gain)
    assert abs(gain - 0.0) < 1e-9

def test_best_split_picks_the_informative_feature():
    X = np.array([
        [1.0, 5.0],
        [2.0, 6.0],
        [8.0, 5.0],
        [9.0, 6.0]
    ])
    y = np.array([0, 0, 1, 1])
    best = best_split(X, y, criterion=entropy)
    # The algorithm must select the first column (feature index 0)
    assert best["feature"] == 0
    # The information gain for feature 0 represents a perfect split (Gain = 1.0)
    assert best["gain"] > 0.99
