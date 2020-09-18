from app import db, ma

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'posts')
    posts = ma.List(ma.HyperlinkRelated("posts_show"))

    
users_schema = UserSchema(many=True)
user_schema = UserSchema(many=False)