from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps
from flask import Flask, jsonify, request
from dotenv import load_dotenv
import flask
import os

load_dotenv()

app = Flask(__name__)
app.debug = True
connection_string = "mongodb+srv://loroz:Luisito1234@ecobill-cluster.mongocluster.cosmos.azure.com/test?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"
if not connection_string:
    raise ValueError("MongoDB connection string not found in environment variables")
app.config["MONGO_URI"] = connection_string


mongoDB_client = PyMongo(app)
db = mongoDB_client.db

@app.route("/")
def root():
    return 'Hi'

@app.route("/user")
def home():
    testQs = db.testQ.find()
    resp = dumps(testQs)
    return resp

if __name__ == "__main__":
    app.run()