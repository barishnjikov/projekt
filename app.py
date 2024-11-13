from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return "Dobrodošli na Flask API za predikciju!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    return jsonify({'prediction': sum(data['input'])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
