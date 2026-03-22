import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

def train_predictive_model(input_path='data/processed/vaccination_coverage_clean.csv', model_output_path='src/models/vaccination_coverage_model.pkl'):
    """
    Trains a simple predictive model to identify key drivers of vaccination coverage.

    Args:
        input_path (str): Path to the cleaned data file.
        model_output_path (str): Path to save the trained model.
    """
    try:
        df = pd.read_csv(input_path)
    except FileNotFoundError:
        print(f"Error: The file at {input_path} was not found.")
        return

    # --- Feature Engineering ---
    # Select features that are likely to influence vaccination coverage
    # For this simple model, we'll use other vaccination types to predict full vaccination
    features = [
        'bcg_vaccination',
        'polio_3_doses',
        'dpt_3_doses',
        'measles_first_dose'
    ]
    target = 'full_vaccination_any_source'

    # Check for missing columns
    if not all(f in df.columns for f in features + [target]):
        print("Error: Dataset is missing required feature or target columns for modeling.")
        print(f"Available columns: {df.columns.tolist()}")
        return

    # Drop rows with missing values in features or target for simplicity
    df_model = df[features + [target]].dropna()

    X = df_model[features]
    y = df_model[target]

    # --- Model Training ---
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Using a RandomForestRegressor as it's robust and provides feature importances
    model = RandomForestRegressor(n_estimators=100, random_state=42, oob_score=True)
    model.fit(X_train, y_train)

    # --- Evaluation ---
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    oob_score = model.oob_score_

    print(f"Model Training Complete.")
    print(f"Mean Squared Error on Test Set: {mse:.2f}")
    print(f"Out-of-Bag R^2 Score: {oob_score:.2f}")

    # --- Feature Importances ---
    feature_importances = pd.DataFrame(model.feature_importances_, index=X.columns, columns=['importance']).sort_values('importance', ascending=False)
    print("\nKey Drivers of Vaccination Coverage:")
    print(feature_importances)


    # --- Save the Model ---
    try:
        joblib.dump(model, model_output_path)
        print(f"\nModel saved to {model_output_path}")
    except Exception as e:
        print(f"Error saving model: {e}")


if __name__ == '__main__':
    # To run this script from the root of the project directory:
    # python src/models/train_model.py
    train_predictive_model()
