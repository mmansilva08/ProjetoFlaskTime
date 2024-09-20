from flask import render_template, request, redirect, session ,url_for
from models import Usuarios, Times
from app import app, db


@app.route('/')
def index():
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))
    lista_times = Times.query.order_by(Times.id_time)
    return render_template('index.html', lista=lista_times)




@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar_time.html')


@app.route('/adicionar', methods=['POST',])
def adicionar_time():
    nome = request.form['nome']
    estado = request.form['estado']
    apelido = request.form['apelido']

    time = Times.query.filter_by(nome_time=nome).first()

    if time:
        return redirect('/')

    novo_time = Times(nome_time=nome, estado_time=estado, apelido_time=apelido)

    db.session.add(novo_time)
    db.session.commit()

    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = Usuarios.query.filter_by(
        email_usuario=request.form['login']
    ).first()

    if usuario and request.form['senha'] == usuario.senha_usuario:
        session['usuario_logado'] = usuario.nome_usuario
        return redirect('/')
    return redirect('/login')


@app.route('/cadastrar-usuario')
def cadastrar_usuario():
    return render_template('cadastrar_usuario.html')


@app.route('/adicionar-usuario', methods=['POST',])
def adicionar_usuario():
    nome_usuario = request.form['nomeUsuario']
    email_usuario = request.form['emailUsuario']
    senha_usuario = request.form['senhaUsuario']

    usuario = Usuarios.query.filter_by(nome_usuario=nome_usuario).first()

    if usuario:
        return redirect('/cadastrar-usuario')

    novo_usuario = Usuarios(nome_usuario=nome_usuario, email_usuario=email_usuario, senha_usuario=senha_usuario)

    db.session.add(novo_usuario)
    db.session.commit()

    return redirect('/login')


@app.route('/sair')
def sair():
    session['usuario_logado'] = None
    return redirect('/login')


@app.route('/editar-time/<int:id>', methods=['GET', 'POST'])
def editar_time(id):
    time = Times.query.get_or_404(id)
    if request.method == 'POST':
        time.nome_time = request.form['nome']
        time.estado_time = request.form['estado']
        time.apelido_time = request.form['apelido']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editar_time.html', time=time)


@app.route('/deletar-time/<int:id>', methods=['POST'])
def deletar_time(id):
    time = Times.query.get_or_404(id)
    db.session.delete(time)
    db.session.commit()
    return redirect(url_for('index'))
