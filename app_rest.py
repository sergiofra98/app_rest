from views import views
from flask import Flask


app = Flask(__name__)

# Agregamos vistas
app.add_url_rule('/', view_func=views.inserta_persona, methods=['POST'])
app.add_url_rule('/<correo>', view_func=views.obten_persona, methods=['GET'])
app.add_url_rule('/<correo>', view_func=views.actualiza_persona, methods=['PUT'])
app.add_url_rule('/<correo>', view_func=views.borra_persona, methods=['DELETE'])
