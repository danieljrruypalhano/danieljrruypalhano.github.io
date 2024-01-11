from flask import Flask, make_response, request, jsonify
from reportlab.pdfgen import canvas
from io import BytesIO

app = Flask(__name__)

@app.route('/gerar_pdf', methods=['POST'])
def gerar_pdf():
    # Obtenha os dados de nome e CPF do corpo da solicitação em formato JSON
    dados = request.get_json()
    
    nome = dados['nome']
    cpf = dados['cpf']

    buffer = BytesIO()

    # Gere o conteúdo do PDF usando o ReportLab
    c = canvas.Canvas(buffer)
    c.drawString(100, 800, f"Nome: {nome}")
    c.drawString(100, 780, f"CPF: {cpf}")
    # Adicione mais detalhes conforme necessário
    c.showPage()
    c.save()

    buffer.seek(0)

    # Crie uma resposta Flask
    response = make_response(buffer.getvalue())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'inline; filename={nome}_{cpf}_exemplo.pdf'

    return response

if __name__ == '__main__':
    app.run(debug=True)