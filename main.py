from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True) #Unique Identifier for each stored video
    name = db.Column(db.String(100), nullable=False) #Max 100 Characters, but title cannot be Null
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name = {self.name}, views = {self.views}, likes = {self.likes}"

db.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the Video is required", required=True) #Argument, Type, and Help Value sent if argument wasn't found
video_put_args.add_argument("views", type=int, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Video name required")
video_update_args.add_argument("views", type=int, help="Video Views required")
video_update_args.add_argument("likes", type=int, help="Likes on the video required")


#videos = {}

#def abortIfVideoNotFound(video_id):
#    if video_id not in videos:
#        abort(404, message="Video ID is not valid")

#def abortIfVideoExists(video_id):
#    if video_id in videos:
#        abort(409, message="Video with same ID already exists")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer

}

class VideoList(Resource):
    @marshal_with(resource_fields)
    def get(self):
        results = VideoModel.query.all()
        return results
api.add_resource(VideoList, "/video/")

class Video(Resource):
    @marshal_with(resource_fields)  #Takes fields and serializes it into a JSON format
    def get(self, video_id):
        if video_id is None:
            results = VideoModel.query.all()
            return results
        result = VideoModel.query.filter_by(id=video_id).first()  #Result is an instance of the VideoModel class
        if not result:
            abort(404, message="Video with that ID could not be found")
        return result
    
    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="This Video ID has already been used")
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video) #Add
        db.session.commit()  #Make permanent
        return video, 201 #Code 201 = Created
    
    #Patching (Update)
    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video doesn't exist")
        if args['name'] is not None:
            result.name = args['name']
        if args['views'] is not None:
            result.views = args['views']
        if args['likes'] is not None:
            result.likes = args['likes']


        db.session.commit()
        
        return result
    
    def delete(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Cannot delete video, because the videoID does not exist")
        db.session.delete(result)
        db.session.commit()
        return '', 204
    
#class HelloWorld(Resource): #Class inherits from resource
    #def get(self, name):
        #return names[name] #{"name": name, "test": test} #Must be JSON serializable
    
api.add_resource(Video, "/video/<int:video_id>") #Register as a resource and how to find it. Here you can define parameters to enter

if __name__ == "__main__":
    app.run(debug=True) #Starts server/Flask application in debug mode

