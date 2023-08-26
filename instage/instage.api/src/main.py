from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import redis
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))

# Connect to Redis and MongoDB
r = redis.Redis(host=redis_host, port=redis_port, db=0)


class Chores(Resource):
    def get(self):
        chore_names = ["AllBlack", "AllStrobe","AllWhite"]
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
