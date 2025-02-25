import joblib
import json
import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the model
file_path = "Recession_Model"  # Change this to the correct file path
try:
    model = joblib.load(file_path)
except Exception as e:
    print(f"Error loading model: {e}")
    sys.exit(1)

# Extract model details
model_details = {
    "Model Type": type(model).__name__,
    "Number of Estimators": getattr(model, "n_estimators", "N/A"),
    "Criterion": getattr(model, "criterion", "N/A"),
    "Max Depth": getattr(model, "max_depth", "N/A"),
    "Min Samples Split": getattr(model, "min_samples_split", "N/A"),
    "Min Samples Leaf": getattr(model, "min_samples_leaf", "N/A"),
    "Max Features": getattr(model, "max_features", "N/A"),
    "Feature Names": getattr(model, "feature_names_in_", "Not available"),
    "Hyperparameters": model.get_params() if hasattr(model, "get_params") else "N/A",
}

# Extract feature importances if available
if hasattr(model, "feature_importances_"):
    model_details["Feature Importances"] = model.feature_importances_.tolist()
    
    # Plot feature importances
    feature_names = model_details["Feature Names"] if model_details["Feature Names"] != "Not available" else range(len(model.feature_importances_))
    plt.figure(figsize=(10, 5))
    plt.barh(feature_names, model.feature_importances_)
    plt.xlabel("Importance")
    plt.ylabel("Feature")
    plt.title("Feature Importances")
    plt.gca().invert_yaxis()
    plt.show()

# Extract classes if available
if hasattr(model, "classes_"):
    model_details["Classes"] = model.classes_.tolist()

# Function to make predictions
def make_prediction(sample_data):
    try:
        prediction = model.predict([sample_data])
        return prediction.tolist()
    except Exception as e:
        return str(e)

# Function to evaluate model performance
def evaluate_model(X_test, y_test):
    try:
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        conf_matrix = confusion_matrix(y_test, y_pred).tolist()
        class_report = classification_report(y_test, y_pred, output_dict=True)
        return {
            "Accuracy": acc,
            "Confusion Matrix": conf_matrix,
            "Classification Report": class_report,
        }
    except Exception as e:
        return str(e)

# Example usage (uncomment and provide valid input to test)
# sample_input = [value1, value2, value3, ...]  # Replace with actual feature values
# print("Prediction:", make_prediction(sample_input))

# Example usage for evaluation (uncomment when you have test data)
# X_test = [...]  # Replace with test feature data
# y_test = [...]  # Replace with test labels
# print("Model Evaluation:", evaluate_model(X_test, y_test))

# Save details to a JSON file
output_file = "model_details.json"
with open(output_file, "w") as json_file:
    json.dump(model_details, json_file, indent=4)

print(f"Model details extracted and saved to '{output_file}'.")

