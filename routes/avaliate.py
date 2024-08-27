from flask import Blueprint, render_template, request, send_file
import random
from database.models.laudo import Laudo
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from database.database import db

avaliate_route = Blueprint("avaliate", __name__)


@avaliate_route.route('/download')
def download_file():
    laudos = Laudo.select()
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    
    # Título do relatório
    pdf.drawString(50, height - 100, "Relatório de Laudos")

    y_position = height - 150  # Posição inicial para os dados
    for laudo in laudos:
        pdf.drawString(50, y_position, f"Código: {laudo.codigo}")
        y_position -= 20
        pdf.drawString(50, y_position, f"Técnico: {laudo.tecnico}")
        y_position -= 20
        pdf.drawString(50, y_position, f"Data de Execução: {laudo.date}")
        y_position -= 20
        pdf.drawString(50, y_position, f"Descrição: {laudo.descricao}")
        y_position -= 40  # Espaço de três linhas antes do próximo laudo
    
    pdf.showPage()
    pdf.save()
    
    buffer.seek(0)
    
    return send_file(buffer, as_attachment=True, download_name="usuarios.pdf", mimetype='application/pdf')

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
    
    if data['codigo'] == '':
        codigoLaudo = gerarId()
    else:
        codigoLaudo = data['codigo']
        
    date_format = datetime.strptime(data['date'], '%Y-%m-%d')
    
    new_laudo = Laudo.create(
        codigo=codigoLaudo, 
        tecnico=data['tecnico'], 
        date=date_format, 
        tipo=data['tipo'], 
        descricao=data['descricao']
    )  

    return render_template('exibirCodigo.html', codigoLaudo=codigoLaudo)    
