import os
from flask import Flask
from routes.bp_usuarios import bp_usuarios
from routes.bp_origens import bp_origens

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', '')

app.register_blueprint(bp_usuarios)
app.register_blueprint(bp_origens)

app.run(debug=True)