from flask import Flask, jsonify, request
from models.user_model import User, user_schema, users_schema
from app import app, db

@app.route('/users')
def users_index():
    users = User.query.all()
    uschema = users_schema.dump(users)
    return jsonify(uschema)

@app.route('/users/show/<int:id>')
def users_show(id):
    try:
        user = User.query.get(id)
        if (user is None):
            raise Exception(f"User was't exists with id={id}")
        return user_schema.dump(user)
    except Exception as e:
        return {'error': str(e)}

@app.route('/users/delete/<int:id>', methods=['DELETE'])
def users_delete(id):
    try:
        user = User.query.get(id)
        if (user is None):
            raise Exception(f'Cound not found post with id={id}')
        
        db.session.delete(user)
        db.session.commit()
        return {'message': 'Success'}
    except Exception as e:
        return {
            'message': str(e)
        }

@app.route('/users/update/<int:id>', methods=['PUT'])
def users_update(id):
    try:
        data = request.get_json()
        email = data['email']
        username = data['username']


        if (email is None and username is None):
            raise Exception('Title and content was not null')

        user = User.query.get(id)
        if (user is None):
            raise Exception(f"Cound not found post with id={id}")
        
        user.username = username
        user.email = email

        db.session.commit()
        return jsonify(user_schema.dump(user))
    except Exception as e:
        return {'error': str(e)}