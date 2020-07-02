from . import app

@app.route('/')
def home():
   return {
      'status': 200,
      'message': "You are running the provider service!"
   }

@app.route('/endpoint01')
def endpoint01():
   return {
      'status': 200,
      'data': 'This is some data from the provider!'
   }