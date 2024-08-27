from flask import Blueprint, render_template, request, send_file
import random
from database.models.laudo import Laudo
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from database.database import db

avaliate_route = Blueprint("avaliate", __name__)


@avaliate_route.route('/download')
def download_file():
    laudos = Laudo.select()
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()

    # Título do relatório
    title = Paragraph("Relatório de Laudos", styles['Title'])
    story.append(title)
    story.append(Paragraph("<br/><br/>", styles['Normal']))  # Espaço entre o título e o conteúdo

    for laudo in laudos:
        content = [
            Paragraph(f"Código: {laudo.codigo}", styles['Normal']),
            Paragraph(f"Técnico: {laudo.tecnico}", styles['Normal']),
            Paragraph(f"Data de Execução: {laudo.date}", styles['Normal']),
            Paragraph(f"Descrição: {laudo.descricao}", styles['Normal']),
            Paragraph("<br/><br/>", styles['Normal'])  # Espaço entre laudos
        ]
        story.extend(content)
    
    doc.build(story)
    
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
