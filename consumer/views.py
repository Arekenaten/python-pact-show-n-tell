from . import app
import requests

@app.route('/')
def home():
   return {
      'status': 200,
      'message': "You are running the consumer service!"
   }

@app.route('/user/<user_id>}')
def get_user(user_id):
   """Fetch a user object by user_name from the provider."""
   uri = 'http://pact_provider_1:3000/users/' + user_id
   return requests.get(uri).json()