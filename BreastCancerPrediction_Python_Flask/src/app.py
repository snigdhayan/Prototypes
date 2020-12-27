import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('./myModel.pkl', 'rb'))

@app.route('/',methods=['GET'])
def home():
    return "Hello World! Ready for input."

@app.route('/predict',methods=['GET', 'POST', 'PUT'])
def predict():
    if request.method == 'GET':
        data = request.args
        prediction = model.predict([np.array(list(data.values()))])
        probability = model.predict_proba([np.array(list(data.values()))])     
    else: # also support json in body via POST and PUT
        data = request.get_json(force=True)
        prediction = model.predict([np.array(list(data.values()))])
        probability = model.predict_proba([np.array(list(data.values()))])

    output = {
        'Prediction': prediction[0],
        'Probability': probability[0].max()
    }
    return jsonify(output)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True) # make the service reachable from outside, if containerized