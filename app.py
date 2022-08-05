from flask import Flask,jsonify,request
from model import getPrediction

app = Flask(__name__)
@app.route('/predict',methods=['POST'])
def displayPrediction():
    image = request.files.get('digit')
    prediction = getPrediction(image)
    return jsonify({
        'result': prediction
    }),2000

if __name__=='__main__':
    app.run(debug=True)