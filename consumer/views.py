from . import app
import requests

@app.route('/')
def home():
   return {
      'status': 200,
      'message': "You are running the consumer service!"
   }

@app.route('/fetch_provider_data')
def get_provider_endpoint():
   r = requests.get('http://pact_provider_1:3000/endpoint01')
   data = r.json()
   return data