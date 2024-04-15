from flask import Flask
from flask_cors import CORS

from controllers.main_controller import main_controller


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


app.register_blueprint(main_controller)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
