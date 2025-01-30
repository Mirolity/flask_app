from flask import Flask, render_template

# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Определяем маршрут для корневого URL
@app.route('/')
def home():
    # Рендерим шаблон index.html
    return render_template('index.html')

# Запускаем приложение, если файл запущен напрямую
if __name__ == '__main__':
    app.run(debug=True)
