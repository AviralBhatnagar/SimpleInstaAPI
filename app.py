from flask import Flask, request
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
from bson.json_util import dumps


app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/Instagram"
mongo = PyMongo(app)
bcrypt = Bcrypt(app)

@app.route('/users',methods=['POST'])
def create_user():
    data = request.json
    id = data['id']
    name = data['name']
    email  = data['email']
    password = bcrypt.generate_password_hash(data['password'])
    mongo.db.Users.insert_one({'id':id,'name':name,'email':email,'password':password})
    return "Done"

@app.route('/users/<int:id>',methods=['GET'])
def get_user(id):
    user = mongo.db.Users.find({'id':id})
    return dumps(user)

@app.route('/posts',methods=['POST'])
def create_post():
    data = request.json
    id = data['id']
    caption = data['caption']
    img_url = data['img_url']
    post_timestamp = data['post_timestamp']
    mongo.db.Posts.insert_one({'id':id,'caption':caption,'img_url':img_url,'post_timestamp':post_timestamp})
    return "Done"

@app.route('/posts/users/<int:id>',methods=['GET'])
def get_posts(id):
    posts = mongo.db.Posts.find({'id':id})
    return dumps(posts)


app.run(debug = True)

