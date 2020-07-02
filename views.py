from . import app

@app.route('/')
def home():
   return "Hello world! I will reload when you change the files!"