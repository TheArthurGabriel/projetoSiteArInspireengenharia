from flask import Blueprint, render_template, request
import random
from database.models.laudo import Laudo

avaliate_route = Blueprint("avaliate", __name__)


@avaliate_route.route('/laudo_form')
def form_laudo():
    return render_template('form.html')

@avaliate_route.route('/laudo_save', methods=['post'])
def generate_laudo():
    data = request.form
    
    def gerarId():
        new_id = ''.join(random.choices('0123456789', k=5))
        try:
            isRepet = Laudo.get(Laudo.codigo == new_id)
            return gerarId()
        except:
            return new_id
        
    codigoLaudo = gerarId()
    
    new_laudo = Laudo.create(
        codigo=codigoLaudo, 
        tecnico=data['tecnico'], 
        date=data['date'], 
        tipo=data['tipo'], 
        descricao=data['descricao']
    )  
      
    return render_template('exibirCodigo.html', codigoLaudo=codigoLaudo)    