
'''
                             APLICATIVO DE OUVIDORIA CONDOMINIO UNIVESP PI2


                VERSÃO      |                       SOBRE                   |       DATA

                            |                                               |
                Inicial     | Login, Menu,  Denuncias, Reclamaçoes, Vendas  |    Novembro, 2024
                            | Sugestoes,  Administração, Inadinplencias     |

'''

from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Página de login sistema
@app.route('/')
@app.route('/login')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Simples verificação de login
        if username == "univesp" and password == "123":
            return redirect(url_for('menu'))
        else:
            return "Login falhou! Usuário ou senha incorretos!!! \n Favor contatar o Administrador (11)94311-7113."

    return render_template('login.html')

 # Página de login do administrador
@app.route('/login_admin')
@app.route('/login_admin', methods=['GET', 'POST'])
def login_admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Simples verificação de login
        if username == "admin" and password == "123":
            return redirect(url_for('menu_admin'))
        else:
            return "Login falhou! Usuário ou senha incorretos!!! \n Favor contatar o Administrador (11)94311-7113."

    return render_template('login_admin.html')

# ----------------------------------------- Configuração do banco de dados MySQL--------------------------------------------------------------

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ouvidoria:aparecido@ouvidoria.mysql.pythonanywhere-services.com/ouvidoria$condominio'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ----------------------------------------- Criando as classes com as tabelas do banco de dados MySQL--------------------------------------------------------------

# Definindo o modelo da tabela sugestoes
class Sugestoes(db.Model):
    __tablename__ = 'sugestoes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    unidade = db.Column(db.String(50))
    sugestao = db.Column(db.Text)

# Definindo o modelo da tabela denuncias
class Denuncias(db.Model):
    __tablename__ = 'denuncias'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    unidade = db.Column(db.String(50))
    denuncia = db.Column(db.Text)

# Definindo o modelo da tabela reclamacoes
class Reclamacoes(db.Model):
    __tablename__ = 'reclamacoes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    unidade = db.Column(db.String(50))
    reclamacao = db.Column(db.Text)

# Definindo o modelo da tabela vendas
class Vendas(db.Model):
    __tablename__ = 'vendas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    unidade = db.Column(db.String(50))
    valor = db.Column(db.Text)
    contato = db.Column(db.Text)

# Definindo o modelo da tabela inadimplentes
class Inadimplentes(db.Model):
    __tablename__ = 'inadimplentes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    unidade = db.Column(db.String(50))
    mes = db.Column(db.Text)



# ----------------------------------------- Criando as rotas --------------------------------------------------------------

# Pagina de Menu
@app.route("/menu")
def menu():
    return render_template("menu.html")

# Pagina de sugestoes
@app.route("/add_sugestoes")
def add_sugestoes():
    return render_template('add_sugestoes.html')

# Rota para exibir a lista de sugestões
@app.route('/sugestoes')
def listar_sugestoes():
    # Consultando todas as sugestões
    sugestoes = Sugestoes.query.all()
    return render_template('lista_sugestoes.html', sugestoes=sugestoes)

# Pagina de reclamacoes
@app.route('/add_reclamacoes')
def add_reclamacoes():
    return render_template('add_reclamacoes.html')

# Rota para exibir a lista de reclamacoes
@app.route('/reclamacoes')
def listar_reclamacoes():
    # Consultando todas as reclamacoes
    reclamacoes = Reclamacoes.query.all()
    return render_template('lista_reclamacoes.html', reclamacoes=reclamacoes)

# Pagina de denuncias
@app.route('/add_denuncias')
def add_denuncias():
    return render_template('add_denuncias.html')

# Rota para exibir a lista de denuncias
@app.route('/denuncias')
def listar_denuncias():
    # Consultando todas as denuncias
    denuncias = Denuncias.query.all()
    return render_template('lista_denuncias.html', denuncias=denuncias)

# Pagina de vendas
@app.route('/add_vendas')
def add_vendas():
    return render_template('add_vendas.html')

# Rota para exibir a lista de denuncias
@app.route('/vendas')
def listar_vendas():
    # Consultando todas as vendas
    vendas = Vendas.query.all()
    return render_template('lista_vendas.html', vendas=vendas)


# Pagina de administracao
@app.route('/administracao')
def administracao():
    return render_template('administracao.html')

# Pagina de inadimplentes
@app.route('/add_inadimplentes')
def add_inadimplentes():
    return render_template('add_inadimplentes.html')

# Rota para exibir a lista de inadimplentes
@app.route('/inadimplentes')
def listar_inadimplentes():
    # Consultando todas as vendas
    inadimplentes = Inadimplentes.query.all()
    return render_template('lista_inadimplentes.html', inadimplentes=inadimplentes)

# Pagina de menu administrador
@app.route('/menu_admin')
def menu_admin():
    return render_template('menu_admin.html')




# ----------------------------------------- Criando os formularios para inserir os dados nas tabelas do banco de dados MySQL--------------------------------------------------------------

# Rota para processar o formulário e inserir dados no banco
@app.route('/inserir_sugestoes', methods=['POST'])
def inserir_sugestoes():
    # Obter os dados do formulário
    nome = request.form['nome']
    unidade = request.form.get('unidade', '')  # Se unidade não for obrigatória
    sugestao = request.form.get('sugestao', '')  # Se sugestão não for obrigatória

    # Criar uma nova entrada e adicionar ao banco de dados
    novo_item = Sugestoes(nome=nome, unidade=unidade, sugestao=sugestao)
    db.session.add(novo_item)
    db.session.commit()

    return redirect(url_for('add_sugestoes'))

# Rota para processar o formulário e inserir dados no banco
@app.route('/inserir_denuncias', methods=['POST'])
def inserir_denuncias():
    # Obter os dados do formulário
    nome = request.form['nome']
    unidade = request.form.get('unidade', '')
    denuncia = request.form.get('denuncia', '')

    # Criar uma nova entrada e adicionar ao banco de dados
    novo_item = Denuncias(nome=nome, unidade=unidade, denuncia=denuncia)
    db.session.add(novo_item)
    db.session.commit()

    return redirect(url_for('add_denuncias'))

# Rota para processar o formulário e inserir dados no banco
@app.route('/inserir_reclamacoes', methods=['POST'])
def inserir_reclamacoes():
    # Obter os dados do formulário
    nome = request.form['nome']
    unidade = request.form.get('unidade', '')
    reclamacao = request.form.get('reclamacao', '')

    # Criar uma nova entrada e adicionar ao banco de dados
    novo_item = Reclamacoes(nome=nome, unidade=unidade, reclamacao=reclamacao)
    db.session.add(novo_item)
    db.session.commit()

    return redirect(url_for('add_reclamacoes'))

# Rota para processar o formulário e inserir dados no banco
@app.route('/inserir_vendas', methods=['POST'])
def inserir_vendas():
    # Obter os dados do formulário
    nome = request.form['nome']
    unidade = request.form.get('unidade', '')
    valor = request.form.get('valor', '')
    contato = request.form.get('contato', '')

    # Criar uma nova entrada e adicionar ao banco de dados
    novo_item = Vendas(nome=nome, unidade=unidade, valor=valor, contato=contato)
    db.session.add(novo_item)
    db.session.commit()

    return redirect(url_for('add_vendas'))

# Rota para processar o formulário e inserir dados no banco
@app.route('/inserir_inadimplentes', methods=['POST'])
def inserir_inadimplentes():
    # Obter os dados do formulário
    nome = request.form['nome']
    unidade = request.form.get('unidade', '')
    mes = request.form.get('mes', '')

    # Criar uma nova entrada e adicionar ao banco de dados
    novo_item = Inadimplentes(nome=nome, unidade=unidade, mes=mes)
    db.session.add(novo_item)
    db.session.commit()

    return redirect(url_for('add_inadimplentes'))


#@app.route('/')
#def hello_world():
#    return 'Hello Team!'



