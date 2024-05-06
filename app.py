from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


model = joblib.load('house_price_prediction.pkl')

@app.route('/predict',methods=['POST'])
def predict():
    data = request.json
    size = int(data['size'])
    bedrooms = int(data['bedrooms'])
    print(f'''

size : {size}
          
bedrooms : {bedrooms} 
          ''')
    
    predicted_price = model.predict([[size,bedrooms]])
    return jsonify({'predicted_price':predicted_price[0]})

if __name__ == '__main__':
    app.run(debug=True)

