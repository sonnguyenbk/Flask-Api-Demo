from flask import Flask, jsonify, request
from models.post_model import Post, post_schema, posts_schema
from app import app, db

@app.route('/posts')
def posts_index():
    posts = Post.query.all()
    print(posts)
    pschema = posts_schema.dump(posts)
    print(pschema)
    return jsonify(pschema)

@app.route('/posts/show/<int:id>')
def posts_show(id):
    try:
        post = Post.query.get(id)
        return post_schema.dump(post)
    except Exception as e:
        return {'error': str(e)}

@app.route('/posts/delete/<int:id>', methods=['DELETE'])
def posts_delete(id):
    try:
        post = Post.query.get(id)
        if (post is None):
            raise Exception(f'Cound not found post with id={id}')
        
        db.session.delete(post)
        db.session.commit()
        return {'message': 'Success'}
    except Exception as e:
        return {
            'message': str(e)
        }

@app.route('/posts/update/<int:id>', methods=['PUT'])
def posts_update(id):
    try:
        data = request.get_json()
        title = data['title']
        content = data['content']

        print(title)
        print(content)

        if (title is None and content is None):
            raise Exception('Title and content was not null')

        post = Post.query.get(id)
        if (post is None):
            raise Exception(f"Cound not found post with id={id}")
        
        post.title = title
        post.content = content

        db.session.commit()
        return jsonify(post_schema.dump(post))
    except Exception as e:
        return {'error': str(e)}