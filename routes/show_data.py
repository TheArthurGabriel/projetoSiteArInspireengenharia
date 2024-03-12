from flask import Blueprint, render_template, request
from database.models.laudo import Laudo

data_route = Blueprint("data", __name__)

@data_route.route('/show', methods=['post'])
def show_data():
    numero_chamado = request.form['numero']
    try:
        laudo = Laudo.get(Laudo.codigo == numero_chamado)
        return render_template('laudo.html', data=laudo)
    except:
        return render_template('index.html', error=True)