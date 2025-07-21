from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    user_id = str(len(users) + 1)
    users[user_id] = data
    return jsonify({"id": user_id, "user": data}), 201

@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    return jsonify(user) if user else ("User not found", 404)

@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id in users:
        users[user_id].update(request.json)
        return jsonify(users[user_id])
    return "User not found", 404

@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in users:
        return jsonify(users.pop(user_id))
    return "User not found", 404

if __name__ == "__main__":
    app.run(debug=True)
