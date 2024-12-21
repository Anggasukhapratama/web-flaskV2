import os
from flask import Flask, render_template
from flask_mysqldb import MySQL
from datetime import datetime

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'atmins'
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'tumanina_db'
    
    # Konfigurasi untuk folder upload
    app.config['UPLOAD_FOLDER'] = os.path.join('app', 'static', 'uploads')
    
    # Buat folder uploads jika belum ada
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    mysql.init_app(app)

    # Import dan register blueprint auth
    from .controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)

    # Import dan register blueprint sentiment
    from .controllers.sentiment_controller import sentiment_bp
    app.register_blueprint(sentiment_bp)

    # Tambahkan filter datetimeformat
    @app.template_filter('datetimeformat')
    def datetimeformat(value, format='%Y-%m-%dT%H:%M'):
        if isinstance(value, datetime):
            return value.strftime(format)
        return value
    
    @app.route('/')
    def index():
        return render_template('landing.html')
    
    return app
