from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)


pipeline = joblib.load('random_forest_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    url = data['url']
    
    feature_vector = extract_features(url)
    
    
    feature_df = pd.DataFrame([feature_vector], columns=get_feature_names())
    
   
    prediction = pipeline.predict(feature_df)
    
    return jsonify(classification=prediction[0])

def extract_features(url):
   
    return [
        url,  
        len(url),
        url.count('.'),
        url.count('/'),
        0, 
        0, 
       
    ]

def get_feature_names():
    
    return [
        'Domain',
        'Having_@_symbol',
        'Having_IP',
        'Path',
        'Prefix_suffix_separation',
        'Protocol',
        'Redirection_//_symbol',
        'Sub_domains',
        'URL_Length',
        'age_domain',
        'dns_record',
        'domain_registration_length',
        'http_tokens',
        'label',
        'statistical_report',
        
       
    ]

if __name__ == '__main__':
    app.run(debug=True)
