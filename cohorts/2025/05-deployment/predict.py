import pickle
from flask import Flask, request, jsonify

# --- Load Models ---
# These models are from the base Docker image (svizor/zoomcamp-model)
model_file = 'model2.bin'
dv_file = 'dv.bin'

# Load the model and the DictVectorizer separately
with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

with open(dv_file, 'rb') as f_in:
    dv = pickle.load(f_in)

# --- Create Flask App ---
app = Flask('subscription_prediction')

@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()

    # Transform the data
    X = dv.transform([client])

    # Make prediction (probability)
    y_pred = model.predict_proba(X)
    prob_positive = y_pred[0, 1] # Probability of "subscription"

    # Also make a hard prediction (True/False)
    subscribed = bool(prob_positive >= 0.5)

    # Format the response
    result = {
        'subscription_probability': round(prob_positive, 3),
        'subscribed': subscribed
    }

    return jsonify(result)

if __name__ == "__main__":
    # This part is for local testing, not used by Gunicorn
    app.run(debug=True, host='0.0.0.0', port=9696)

