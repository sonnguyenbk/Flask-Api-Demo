from app import db, ma

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship("User", backref="posts")

class PostSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author')
        
    author = ma.HyperlinkRelated('users_show')


posts_schema = PostSchema(many=True)
post_schema = PostSchema(many=False)
