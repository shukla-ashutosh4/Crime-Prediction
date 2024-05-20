import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

def load_data(file_path):
    """Load data from CSV file."""
    return pd.read_csv(file_path)

def clean_data(data):
    """Remove missing values."""
    data.dropna(inplace=True)
    return data

def encode_categorical(data):
    """One-hot encode categorical features."""
    return pd.get_dummies(data)

def scale_data(data, method='standard'):
    """Scale numerical features."""
    if method == 'standard':
        return (data - data.mean()) / data.std()
    elif method == 'minmax':
        return (data - data.min()) / (data.max() - data.min())

def select_features(X, y, k=10):
    """Select k best features based on chi-square test."""
    chi2_scores = pd.DataFrame({'feature': X.columns, 'chi2_score': np.zeros(len(X.columns))})
    for feature in X.columns:
        observed = pd.crosstab(X[feature], y)
        chi2, _, _, _ = chi2_contingency(observed)
        chi2_scores.loc[chi2_scores['feature'] == feature, 'chi2_score'] = chi2
    selected_features = chi2_scores.sort_values(by='chi2_score', ascending=False)['feature'][:k].tolist()
    return X[selected_features]

def handle_imbalance(X, y):
    """Handle class imbalance using SMOTE."""
    from imblearn.over_sampling import SMOTE
    smote = SMOTE(random_state=42)
    return smote.fit_resample(X, y)

def split_data(data, target_column, test_size=0.2, random_state=42):
    """Split data into train and test sets."""
    X = data.drop(columns=[target_column])
    y = data[target_column]
    np.random.seed(random_state)
    mask = np.random.rand(len(data)) < (1 - test_size)
    return X[mask], X[~mask], y[mask], y[~mask]

# Usage example:
file_path = (r"C:\Program Files\GitHub\KSP\Cleaned_data.csv" , encoding='latin1')
data = load_data(file_path)
data = clean_data(data)
data = encode_categorical(data)
X_train, X_test, y_train, y_test = split_data(data, target_column='target_column_name')
X_train, y_train = handle_imbalance(X_train, y_train)
X_train_scaled = scale_data(X_train, method='standard')
X_test_scaled = scale_data(X_test, method='standard')
X_train_selected = select_features(X_train_scaled, y_train, k=10)