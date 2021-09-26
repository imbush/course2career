import json

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


posts = dict()

comments = dict()

post_id_counter = 0
comment_id_counter = 0

@app.route("/")
def homePage():
    return "Welcome to the api for our BRH21 hack!"


# your routes here
@app.route("/api/courses/", methods=["GET"])
def getAllCourses():
    with open("coursesWithKW.json", 'r') as inJSON:
        return json.dumps(inJSON), 200

@app.route("/api/posts/<subject>/<int:course_id>/", methods=["GET"])
def get_course(subject, course_id):
    with open("coursesWithKW.json", 'r') as inJSON:
        if not course.get(subject):
            return json.dumps({"error": "Post not found"}), 404
            
    return json.dumps(posts.get(post_id)), 200

    return json.dumps(inJSON), 200

@app.route("/api/posts/<int:post_id>/", methods=["DELETE"])
def delete_post(post_id):
    post = posts.get(post_id)
    if not post:
        return json.dumps({"error": "Post not found"}), 404
    del posts[post_id]
    return json.dumps(post), 200

@app.route("/api/posts/<int:post_id>/comments/", methods=["GET"])
def get_comments(post_id):

    
    if not posts.get(post_id):
        return json.dumps({"error": "Post not found"}), 404
    response = {
        "comments": list(comments.get(post_id).values())
    }
    return json.dumps(response), 200

@app.route("/api/posts/<int:post_id>/comments/", methods=["POST"])
def create_comment(post_id):
    global comment_id_counter
    body = json.loads(request.data)
    if not (body.get("text") and body.get("username")):
        return json.dumps({"error": "Invalid request"}), 404
    if not posts.get(post_id):
        return json.dumps({"error": "Post not found"}), 404

    response = {
        "id": comment_id_counter,
        "upvotes": 1,
        "text": body.get("text"),
        "username": body.get("username")
    }
    comments[post_id][comment_id_counter] = response
    comment_id_counter += 1
    return json.dumps(response), 201

@app.route("/api/posts/<int:post_id>/comments/<int:comment_id>/", methods=["POST"])
def edit_comment(post_id, comment_id):
    body = json.loads(request.data)
    if not (comments.get(post_id) and comments.get(post_id).get(comment_id)):
        return json.dumps({"error": "Could not find post or comment"}), 404
    if not body.get("text"):
        return json.dumps({"error": "Invalid request"})
    comments[post_id][comment_id]["text"] = body.get("text")
    response = comments[post_id][comment_id]
    return json.dumps(response), 200



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
