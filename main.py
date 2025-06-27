import logging
from flask import Flask, request, jsonify

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask работает!'

@app.route('/echo', methods=['POST'])
def echo_json():
    if not request.is_json:
        return jsonify({'error': 'Ожидался JSON'}), 400
    data = request.get_json()
    # Логируем все атрибуты
    logging.info(f"Получен JSON: {data}")
    # Формируем строку с атрибутами и их значениями
    attrs = '\n'.join([f"{k}: {v}" for k, v in data.items()])
    return f"Получены атрибуты:\n{attrs}", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
