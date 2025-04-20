"""
Unit tests for Quantum Adversarial Threat Intelligence (QATI) utilities.
"""
import pytest
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from qati_utils import (
    load_data,
    preprocess_data,
    split_data,
    evaluate_model,
    save_model,
    load_model,
    normalize_data,
    check_data_integrity
)
import os
import joblib

@pytest.fixture
def sample_data():
    """Fixture to create a sample dataset for testing."""
    X, y = make_classification(n_samples=100, n_features=20, n_classes=2, random_state=42)
    df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(20)])
    df['target'] = y
    return df

def test_load_data(sample_data):
    """Test loading data from a CSV file."""
    sample_data.to_csv('test_data.csv', index=False)
    loaded_data = load_data('test_data.csv')
    assert loaded_data.shape == sample_data.shape
    assert all(loaded_data.columns == sample_data.columns)
    os.remove('test_data.csv')  # Clean up

def test_preprocess_data(sample_data):
    """Test preprocessing of data."""
    X, y = preprocess_data(sample_data, target_column='target')
    assert X.shape[0] == sample_data.shape[0]
    assert y.shape[0] == sample_data.shape[0]
    assert X.shape[1] == 20  # Number of features

def test_split_data(sample_data):
    """Test splitting of data."""
    X, y = preprocess_data(sample_data, target_column='target')
    X_train, X_test, y_train, y_test = split_data(X, y)
    assert X_train.shape[0] + X_test.shape[0] == X.shape[0]
    assert y_train.shape[0] + y_test.shape[0] == y.shape[0]

def test_evaluate_model(sample_data):
    """Test evaluation of a model."""
    from sklearn.linear_model import LogisticRegression
    X, y = preprocess_data(sample_data, target_column='target')
    X_train, X_test, y_train, y_test = split_data(X, y)
    
    model = LogisticRegression()
    model.fit(X_train, y_train)
    accuracy = evaluate_model(model, X_test, y_test)
    assert accuracy >= 0.0  # Accuracy should be non-negative

def test_save_load_model(sample_data):
    """Test saving and loading of a model."""
    from sklearn.linear_model import LogisticRegression
    X, y = preprocess_data(sample_data, target_column='target')
    X_train, X_test, y_train, y_test = split_data(X, y)
    
    model = LogisticRegression()
    model.fit(X_train, y_train)
    save_model(model, 'test_model.pkl')
    
    loaded_model = load_model('test_model.pkl')
    assert isinstance(loaded_model, LogisticRegression)
    os.remove('test_model.pkl')  # Clean up

def test_normalize_data(sample_data):
    """Test normalization of data."""
    X, y = preprocess_data(sample_data, target_column='target')
    X_normalized = normalize_data(X)
    assert np.allclose(np.mean(X_normalized, axis=0), 0, atol=1e-1)  # Mean should be close to 0
    assert np.allclose(np.std(X_normalized, axis=0), 1, atol=1e-1)    # Std should be close to 1

def test_check_data_integrity(sample_data):
    """Test data integrity check."""
    assert check_data_integrity(sample_data) is True
    sample_data_with_nan = sample_data.copy()
    sample_data_with_nan.iloc[0, 0] = np.nan
    assert check_data_integrity(sample_data_with_nan) is False

if __name__ == "__main__":
    pytest.main()
