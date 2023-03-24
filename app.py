from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/books', methods=['POST'])
def add_book():
    title = request.json['title']
    author = request.json['author']
    mongo.db.books.insert({'title': title, 'author': author})
    return jsonify({'message': 'Book added successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
