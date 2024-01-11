from flask import Flask, make_response, request, jsonify
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from io import BytesIO

app = Flask(__name__)

@app.route('/gerar_pdf', methods=['POST'])
def gerar_pdf():
    # Substitua a URL de exemplo pela URL da imagem que deseja utilizar
    url_imagem = 'https://www.ufmt.br/ocs/images/phocagallery/galeria2/thumbs/phoca_thumb_l_image03_grd.png'

    # Obtenha os dados de nome do corpo da solicitação em formato JSON
    dados = request.get_json()
    nome = dados['nome']

    buffer = BytesIO()

    # Gere o conteúdo do PDF usando o ReportLab
    c = canvas.Canvas(buffer, pagesize=letter)

    # Adicione imagem
    try:
        image_data = ImageReader(url_imagem)
        c.drawImage(image_data, 0, 0, width=1000, height=10000)  # Ajuste as coordenadas conforme necessário
    except Exception as e:
        print(f"Erro ao adicionar imagem: {e}")

    # Adicione texto
    c.drawString(100, 300, f"Nome: {nome}")

    # Adicione mais detalhes conforme necessário
    c.save()

    buffer.seek(0)

    # Crie uma resposta Flask
    response = make_response(buffer.getvalue())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'inline; filename={nome}_exemplo.pdf'

    return response

if __name__ == '__main__':
    app.run(debug=True)