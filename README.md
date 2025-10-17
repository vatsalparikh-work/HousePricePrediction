# HousePricePrediction

# Banglore House Price Prediction

A minimal project for exploring and predicting Banglore housing prices using a trained model artifact and a simple Python app for local inference and demos.

## Repository contents

- app.py — application entry point for local run.
- Bengaluru_House_Data.csv — source dataset used for EDA/training.
- columns.json — feature/column metadata used at inference.
- banglore_home_prices_model.pickle — trained model artifact for predictions.

## Dataset overview

The dataset includes fields such as: area_type, availability, location, size, society, total_sqft, bath, balcony, and price.  
Notes:
- Some rows contain missing values (for example, blank society), so cleaning/imputation may be required before retraining.
- total_sqft can include ranges or non‑numeric tokens (e.g., “1565 - 1595”), so normalize to numeric during preprocessing.

## Quick start

1) Environment
- Python 3.9+ recommended.
- If a requirements.txt exists, run:

python -m venv .venv
.venv\Scripts\activate # Windows
source .venv/bin/activate # macOS/Linux
pip install -r requirements.txt

- Without a requirements.txt, a minimal stack is:
pip install numpy pandas scikit-learn flask

2) Run the app
Open the printed local URL if a server starts, or follow terminal prompts if it’s CLI-based.

## Programmatic inference example

import json, pickle
import numpy as np

Load model
with open('banglore_home_prices_model.pickle', 'rb') as f:
model = pickle.load(f)

Load column metadata (adjust the key to your schema)
with open('columns.json', 'r') as f:
cols = json.load(f) # e.g., cols["data_columns"] if your JSON uses that key

Build a feature vector in the exact order expected by the model
x = np.zeros(len(cols if isinstance(cols, list) else cols.get('data_columns', [])))

Fill indices based on your preprocessing and encodings
x[idx_total_sqft] = 1200
x[idx_bath] = 2
x[idx_bhk] = 3
... one‑hot indices for categoricals like location/area_type
Predict
print(float(model.predict([x])))
text

## Retraining notes

- Clean and normalize total_sqft to numeric and handle missing values before training.
- Ensure columns.json mirrors the final feature order used by the training pipeline.
- When retraining, export a new pickle and update columns.json to keep inference consistent.

## Suggested structure

- data/: raw and processed datasets
- notebooks/: EDA and experiments
- src/: feature engineering and training code
- models/: serialized artifacts (pickle and metadata)

## Contributing

Issues and pull requests are welcome. Please describe changes clearly and include steps to reproduce or validate results.

## License

Add a LICENSE file or state the license here (e.g., MIT).
