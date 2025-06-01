from flask import Flask
from flask_code.routes import routes

def flask_main():
    app = Flask(__name__)
    app.register_blueprint(routes)
    return app

if __name__ == '__main__':
    app = flask_main()
    app.run(debug=True, host='0.0.0.0', port=5000)
