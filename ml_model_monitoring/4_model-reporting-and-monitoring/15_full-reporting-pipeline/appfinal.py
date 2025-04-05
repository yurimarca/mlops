from flask import Flask, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

@app.route('/prediction', methods=['GET'])
def predict():
    try:
        # Load the deployed model
        with open('deployedmodel.pkl', 'rb') as model_file:
            model = pickle.load(model_file)
        
        # Load the dataset
        data = pd.read_csv('predictiondata.csv')
        
        # Make predictions
        predictions = model.predict(data)
        
        # Return predictions as a JSON response
        return jsonify(predictions.tolist())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)