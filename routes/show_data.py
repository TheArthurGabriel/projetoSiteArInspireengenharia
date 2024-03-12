from flask import Blueprint, render_template, request
from database.models.laudo import Laudo

data_route = Blueprint("data", __name__)

@data_route.route('/show', methods=['post'])
def show_data():
    numero_chamado = request.form['numero']
    
    laudos = Laudo.select().where(Laudo.codigo == numero_chamado)
    if len(laudos) > 0:
        return render_template('laudo.html', data=laudos)
    else:
        return render_template('homepage.html', error=True)

        
    
    