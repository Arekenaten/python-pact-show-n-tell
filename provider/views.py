from . import app

@app.route('/')
def home():
   return "Congrats! You're running the example test suite to show off pact testing."

@app.route('/endpoint01')
def endpoint01():
   return {
      'status': 200,
      'body': 'You got to endpoint01. Yay!'
   }