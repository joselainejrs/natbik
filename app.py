from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)
#criação da rota par adicionar a imagem 
UPLOAD_FOLDER = 'static/imagens/comentarios/'

#Cria uma Classe
class Acesso:
    def __init__(self, email, senha, tipo) -> None:
        self.email = email
        self.senha = senha
        self.tipo = tipo
usuario1 = Acesso("joselaine@gamil.com", "123", "Estudante")
lista_usuario = [usuario1]

class Comentario:
    def __init__(self, nome, descricao, filename) -> None:
        self.nome = nome
        self.descricao = descricao
        self.filename = filename
        
com1 = Comentario("Lorena Lucco", "Use o produtos dessa empresa, entrega rápida e facilitada", "img-comentarios.png")
com2 = Comentario("Marlene Silva", "Use o produtos dessa empresa, entrega rápida e facilitada", "m 1.png")
com3 = Comentario("Julia Marcela", "Use o produtos dessa empresa, entrega rápida e facilitada", "m 2.png")
com4 = Comentario("Domingas Elias", "Use o produtos dessa empresa, entrega rápida e facilitada", "m 3.png")
lista_comentarios = [com1, com2, com3, com4]


@app.route('/home')
def home():  # put application's code here

    cards_beneficios = [
        {
            "file":"img 4.png",
            "comentario": "contra o surgimento de doenças coronarianas, pressão alta, AVC, demência, diabetes, síndrome metabólica, câncer de colón e de mama."
        },
        {
            "file":"img 5.png",
            "comentario": "O ganho de massa muscular melhora a capacidade física e a coordenação motora devido a maior força, equilíbrio e resistência. Quem adota a prática para a vida, pode evitar (ou retardar) a ocorrência de sarcopenia “perda da força e massa muscular que ocorre na terceira idade e comasdoenças crônicas."
        },
        {
            "file":"img 4.png",
            "comentario": "Com a melhora na resistência cardiorrespiratória há menossensação de cansaço, menos preguiça, redução de sintomas como a falta de ar e a fadiga. Além disso, a prática também pode reduzir dores corporais e melhorar a funcionalidade geral."
        },
    ]
    return render_template('index.html', nome_da_tela='Joselaine', cards_beneficios=cards_beneficios, lista_comentarios=lista_comentarios)

@app.route('/bicicleta')
def bicicleta():  # put application's code here
    cards_bikes = [
        {
            "nome": "Bicicleta Aro 29 KRW Alumínio",
            "valor":"R$ 804, 00"
        },
        {
            "nome": "Bicicleta Aro 29 KRW Alumínio",
            "valor":"R$ 804, 00"
        },
        {
            "nome": "Bicicleta Aro 29 KRW Alumínio",
            "valor":"R$ 804, 00"
        },

    ]
    return render_template('bicicleta.html', nome_da_tela="Bicicletas", cards_bikes=cards_bikes)

@app.route('/login')
def login(): 
    return render_template('login.html')

@app.route('/acesso', methods=['POST',])
def logado():
    email = request.form['email']
    senha = request.form['senha']
    tipo = request.form['tipo']
    for usuario in lista_usuario:
        if usuario.email == email and usuario.senha == senha and usuario.tipo == tipo:
            return render_template('index.html')    
        

@app.route('/comentarios')
def tela_comentario(): 
    return render_template('comentarios.html')
        
@app.route('/criar_comentarios', methods=['POST',])
def comentarios():
    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    file = request.files.get('file')
    print('1')
    if not os.path.exists(UPLOAD_FOLDER):
        print('passou')
        os.makedirs(UPLOAD_FOLDER)
    if file:
        print('entrou aqui')
        # print({file.filename})
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        comentario = Comentario(nome, descricao, file.filename)
        lista_comentarios.append(comentario)
    else:
        print('UPLOAD_FOLDER')
        return "Nenhum arquivo selecionado!", 400

   
    return redirect('/home')
    

@app.route('/bicicleta/compra')
def compra():  # put application's code here
    return render_template('compra.html')



if __name__ == '__main__':
    app.run(debug=True)
