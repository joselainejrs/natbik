from flask import Flask, render_template,jsonify

app = Flask(__name__)


@app.route('/home')
def home():  # put application's code here
    lista_comentarios = [
        {
            "nome": "Lorena Lucco",
            "imagem": "../static/img/img-comentarios.png",
            "descricao": "Use o produtos dessa empresa, entrega rápida e facilitada"
        },
        {
            "nome": "Marlene Silva",
            "imagem": "../static/img/m 1.png",
            "descricao": "Use o produtos dessa empresa, entrega rápida e facilitada"
        },
        {
            "nome": "Julia Marcela",
            "imagem": "../static/img/m 2.png",
            "descricao": "Use o produtos dessa empresa, entrega rápida e facilitada"
        },
        {
            "nome": "Domingas Elias",
            "imagem": "../static/img/m 3.png",
            "descricao": "Use o produtos dessa empresa, entrega rápida e facilitada"

        },
    ]

    cards_beneficios = [
        {
            "img":"../static/img/img 4.png",
            "comentario": "contra o surgimento de doenças coronarianas, pressão alta, AVC, demência, diabetes, síndrome metabólica, câncer de colón e de mama."
        },
        {
            "img":"../static/img/img 5.png",
            "comentario": "O ganho de massa muscular melhora a capacidade física e a coordenação motora devido a maior força, equilíbrio e resistência. Quem adota a prática para a vida, pode evitar (ou retardar) a ocorrência de sarcopenia “perda da força e massa muscular que ocorre na terceira idade e comasdoenças crônicas."
        },
        {
            "img":"../static/img/img 4.png",
            "comentario": "Com a melhora na resistência cardiorrespiratória há menossensação de cansaço, menos preguiça, redução de sintomas como a falta de ar e a fadiga. Além disso, a prática também pode reduzir dores corporais e melhorar a funcionalidade geral."
        },
    ]
    return render_template('index.html', nomeLoja='Joselaine', lista_comentarios=lista_comentarios, cards_beneficios=cards_beneficios)

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
    return render_template('bicicleta.html', cards_bikes=cards_bikes)

@app.route('/login')
def login():  # put application's code here
    return render_template('login.html')

@app.route('/bicicleta/compra')
def compra():  # put application's code here
    return render_template('compra.html')



if __name__ == '__main__':
    app.run()
