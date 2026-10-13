from flask import Flask, jsonify, request

app = Flask(__name__)

# Простая база данных в памяти
users_db = [
    {"id": 1, "name": "Иван", "email": "ivan@test.com"},
    {"id": 2, "name": "Анна", "email": "anna@test.com"}
]

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users_db), 200

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    new_user = {
        "id": len(users_db) + 1,
        "name": data["name"],
        "email": data["email"]
    }
    users_db.append(new_user)
    return jsonify(new_user), 201

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users_db
    users_db = [u for u in users_db if u["id"] != user_id]
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    # Внимание: запуск с debug=True может обнаруживаться анализаторами как потенциальный риск в продакшене
    app.run(host='0.0.0.0', port=5000, debug=True)