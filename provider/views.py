from . import app, db
from flask import current_app, request, jsonify
from sqlalchemy import exc
from .models import User

@app.route('/')
def home():
   current_app.logger.info('Testing clogs')

   return {
      'status': 200,
      'message': "You are running the provider service!"
   }

@app.route('/add_user', methods=['POST'])
def add_user():
   try:
      data = request.get_json()
      current_app.logger.info(data)
      new_user = User(
         id=data.get('id'),
         username=data.get('username'),
         email=data.get('email')
      )
      db.session.add(new_user)
      db.session.commit()

      return {200, 'okay'}

   except exc.IntegrityError as e:
      return {
         'status': 500,
         'error': e.args
      }


@app.route('/users/<id>')
def return_user(id):
   user = User.query.get(id) or ""

   if user:
      return {
         'status': 200,
         'user_id': user.id,
         'user_name': user.username,
         'email': user.email
      }
   else:
      return {'status': 404}