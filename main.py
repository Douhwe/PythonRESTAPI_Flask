from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the Video is required", required=True) #Argument, Type, and Help Value sent if argument wasn't found
video_put_args.add_argument("views", type=int, help="Views of the vided is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the vdeo", required=True)
videos = {}

def abortIfVideoNotFound(video_id):
    if video_id not in videos:
        abort(404, message="Video ID is not valid")

def abortIfVideoExists(video_id):
    if video_id in videos:
        abort(409, message="Video with same ID already exists")

class Video(Resource):
    def get(self, video_id):
        abortIfVideoNotFound(video_id)
        return videos[video_id]
    
    def put(self, video_id):
        abortIfVideoExists(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201 #Code 201 = Created
    
    def delete(self, video_id):
        abortIfVideoNotFound(video_id)
        del videos[video_id]
        return '', 204
    
#class HelloWorld(Resource): #Class inherits from resource
    #def get(self, name):
        #return names[name] #{"name": name, "test": test} #Must be JSON serializable
    
api.add_resource(Video, "/video/<int:video_id>") #Register as a resource and how to find it. Here you can define parameters to enter

if __name__ == "__main__":
    app.run(debug=True) #Starts server/Flask application in debug mode

