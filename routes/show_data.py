from flask import Blueprint, render_template, request
from database.models.laudo import Laudo
from database.database import db
from datetime import datetime

data_route = Blueprint("data", __name__)

@data_route.route('/show', methods=['post'])
def show_data():
    numero_chamado = request.form['numero']
    
    laudos = Laudo.select().where(Laudo.codigo == numero_chamado).order_by(Laudo.date.desc())
    laudos_ordenados = sorted(laudos, key=lambda laudo: laudo.date, reverse=True)

    if len(laudos) > 0:
        return render_template('laudo.html', data=laudos_ordenados)
    else:
        return render_template('homepage.html', error=True)

        
@data_route.route('/<int:id>/delete', methods=['DELETE'])
def delete(id):
    target = Laudo.get_by_id(id)
    target.delete_instance()
    return 'ok'
