import pymongo
from pymongo import MongoClient
from flask import Flask, Request

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb+srv://terekhovhd:GreighT131@cluster0.g38mbdx.mongodb.net/test"
mongo = pymongo(app)

@app.route('/upload', methods=['POST'])
def save_data():
    

if __name__ == '__main__':
    app.run()

