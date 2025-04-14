from flask import Flask, render_template, request, redirect, url_for
import os

# Criando o app Flask
app = Flask(__name__)

# Caminho onde as imagens serão salvas
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Tipos de arquivos permitidos (fotos e vídeos)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'webm', 'mov'}

# Verifica se o arquivo é permitido
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Cria a pasta de upload se ela não existir
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Rota principal
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return redirect(url_for('index'))
    
    # Lista os arquivos de imagem já salvos
    photos = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', photos=photos)

# Iniciar o servidor local
if __name__ == '__main__':
    app.run(host='192.168.1.111', port=5000, debug=True)
