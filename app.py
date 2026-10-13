from flask import Flask, jsonify

app = Flask(__name__)

# Добавляем маршрут для главной страницы, чтобы не было ошибки 404
@app.route('/')
def home():
    return """
    <h1>Лабораторная работа № 5: Безопасность и CI/CD</h1>
    <p>Приложение успешно запущенно!</p>
    <ul>
        <li><a href="/api/users">Список пользователей (API)</a></li>
    </ul>
    """

# Ваш существующий эндпоинт (пример)
@app.route('/api/users', methods=['GET'])
def get_users():
    users = [
        {"id": 1, "name": "Anuar"},
        {"id": 2, "name": "Admin"}
    ]
    return jsonify(users)

if __name__ == '__main__':
    # Оставляем запуск
    app.run(host='0.0.0.0', port=5000, debug=True)