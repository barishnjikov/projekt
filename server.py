import pickle
from flask import Flask, request, jsonify

# Učitavanje modela
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Kreiranje Flask aplikacije
app = Flask(__name__)

# Definiranje rute za početnu stranicu
@app.route('/')
def home():
    return "Dobrodošli na Flask API za predikciju!"

# Definiranje rute za predikciju
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data['input']])
    return jsonify({'prediction': int(prediction[0])})  # Konverzija u regularni int

if __name__ == '__main__':
    app.run(debug=True)
