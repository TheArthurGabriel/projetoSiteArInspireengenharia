from flask import Blueprint, render_template, request
import random
from database.models.laudo import Laudo
from datetime import datetime

avaliate_route = Blueprint("avaliate", __name__)


@avaliate_route.route('/laudo_form')
def form_laudo():
    return render_template('form.html')

@avaliate_route.route('/laudo_save', methods=['post'])
def generate_laudo():
    data = request.form
    
    date_str = data['date']
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    data_formatada = date_obj.strftime('%d/%m/%Y')
    
    def gerarId():
        new_id = ''.join(random.choices('0123456789', k=5))
        try:
            isRepet = Laudo.get(Laudo.codigo == new_id)
            return gerarId()
        except:
            return new_id
    
    if data['codigo'] == '':
        codigoLaudo = gerarId()
    else:
        codigoLaudo = data['codigo']
    
    new_laudo = Laudo.create(
        codigo=codigoLaudo, 
        tecnico=data['tecnico'], 
        date=data_formatada, 
        tipo=data['tipo'], 
        descricao=data['descricao']
    )  
      
    return render_template('exibirCodigo.html', codigoLaudo=codigoLaudo)    