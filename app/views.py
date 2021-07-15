from flask_pymongo import PyMongo

from app import app

# Connection String
app.config["MONGO_URI"] = 'mongodb://root:123456@localhost:27017/maktab?authSource=admin'

mongo = PyMongo(app)


@app.route('/')
def index():
    return 'Index'


@app.route('/all')
def show_all():
    all_docs = mongo.db.flask.find()
    return {
        'name': all_docs[0]['name']
    }