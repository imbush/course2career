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
        return json.load(inJSON), 200

@app.route("/api/courses/<subject>/<int:course_id>/", methods=["GET"])
def get_course(subject, course_id):
    with open("coursesWithKW.json", 'r') as inJSON:
        subjectDict = json.load(inJSON)
        print(subjectDict.get(subject), subjectDict.get(subject)["courses"])
        if not (subjectDict.get(subject) and subjectDict.get(subject)["courses"].get(course_id)):
            return json.dumps({"error": "Course not found"}), 404
        return json.dumps(subjectDict.get(subject)["courses"].get(course_id)), 200

@app.route("/api/courses/", methods=["GET"])
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


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
