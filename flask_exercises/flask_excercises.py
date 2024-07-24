from flask import Flask, request, jsonify


class UserDatabase:
    def __init__(self):
        self.users = {}

    def create_user(self, name):
        self.users[name] = {"age": None}
        return {"data": f"User {name} is created!"}, 201

    def get_user(self, name):
        if name not in self.users:
            return {"error": "User not found"}, 404
        return {"data": f"My name is {name}"}, 200

    def update_user(self, old_name, new_name):
        if old_name not in self.users:
            return {"error": "User not found"}, 404
        if new_name in self.users:
            return {"error": "User already exists"}, 400
        self.users[new_name] = self.users.pop(old_name)
        return {"data": f"My name is {new_name}"}, 200

    def delete_user(self, name):
        if name not in self.users:
            return {"error": "User not found"}, 404
        del self.users[name]
        return '', 204


user_db = UserDatabase()


class FlaskExercise:
    @staticmethod
    def configure_routes(app: Flask) -> None:
        @app.route('/user', methods=['POST'])
        def create_user():
            data = request.get_json()
            if 'name' not in data:
                return jsonify({"errors": {"name": "This field is required"}}), 422

            name = data['name']
            result, status_code = user_db.create_user(name)
            return jsonify(result), status_code

        @app.route('/user/<name>', methods=['GET'])
        def get_user(name):
            result, status_code = user_db.get_user(name)
            return jsonify(result), status_code

        @app.route('/user/<name>', methods=['PATCH'])
        def update_user(name):
            data = request.get_json()
            new_name = data.get('name')
            if not new_name:
                return jsonify({"errors": {"name": "This field is required"}}), 422

            result, status_code = user_db.update_user(name, new_name)
            return jsonify(result), status_code

        @app.route('/user/<name>', methods=['DELETE'])
        def delete_user(name):
            result, status_code = user_db.delete_user(name)
            return '', status_code
