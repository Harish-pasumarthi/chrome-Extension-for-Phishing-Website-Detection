import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import FunctionTransformer
import joblib


dataset = pd.read_csv('Phishing_Legitimate_full.csv')
for col in dataset.columns:
    if dataset[col].dtype == 'object':
      
        dataset[col] = pd.to_numeric(dataset[col], errors='coerce')


X = dataset.drop("label", axis=1)
y = dataset["label"]

categorical_features = [col for col in X.columns if X[col].dtype == 'object']


preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse=False), categorical_features),  # Handle unknown categories and output as dense array
        ('num', SimpleImputer(strategy='mean'), [col for col in X.columns if X[col].dtype in ['int64', 'float64']])  # Handle missing values in numeric features
    ],
    remainder='passthrough' 
)


pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipeline.fit(X_train, y_train)
joblib.dump(pipeline, "random_forest_model.pkl")

print("Model trained and saved successfully.")
