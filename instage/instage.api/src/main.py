from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import redis
import pymongo
import os
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))
mongo_host = os.getenv("MONGO_HOST", "localhost")
mongo_port = int(os.getenv("MONGO_PORT", 27017))

# Connect to Redis and MongoDB
r = redis.Redis(host=redis_host, port=redis_port, db=0)
mongo_client = MongoClient(mongo_host, mongo_port)
# mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo_client["instage"]  # Name of your MongoDB database
chores_collection = db["chores"]

class Chores(Resource):
    def get(self):
        # Retrieve all names from the 'chores' collection
        chores = list(chores_collection.find({}, {"_id": 0, "name": 1}))
        chore_names = [chore['name'] for chore in chores]
        return jsonify(chore_names)
    
    def post(self):
        # Get 'name' from payload and set it in Redis
        name = request.json.get('name')
        if name:
            r.set("current_chore", name)
            return {"message": "Chore set successfully!"}, 200
        else:
            return {"message": "Name not provided!"}, 400
        

api.add_resource(Chores, '/chores')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
