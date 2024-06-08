from flask import render_template, request, redirect, url_for, flash, session 
from app import app, db
from sqlalchemy.exc import SQLAlchemyError
from models import Problema, Solucao, Tag



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar_problema')
def inicio_cadastro():
    consulta_db = Tag.query.all()
    return render_template('cadastro/cad_problema.html', consulta_db=consulta_db)


@app.route('/envio_problema', methods=['POST'])
def problemas():

    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        escritor = request.form['escritor']
        nome_tag = request.form['tag']

        novo_problema = Problema(titulo=titulo, descricao=descricao, escritor=escritor)
        tag_existente = Tag.query.filter_by(nome_tag=nome_tag).first()
    
        if tag_existente:
            novo_problema.tags.append(tag_existente)

        try:    
           db.session.add(novo_problema)
           db.session.commit() 
           flash('Cadastrado com sucesso :)', category='success')
        except SQLAlchemyError as e:
            db.session.rollback()
            flash('Erro no cadastro (: ):{str(e)}', category='error')

        return redirect(url_for('inicio_cadastro'))


@app.route('/problemas_cadastrados', methods=['GET'])
def problemas_cadastrados():
    problemas = Problema.query.all()
    ids_problemas = [problema.id for problema in problemas]
    print(ids_problemas)
    return render_template('registrados/problemas_cadastrados.html', problemas=problemas, ids_problemas=ids_problemas)



@app.route('/dashboard')
def dash(): 
    all_tags = Tag.query.all()
    ocorrencia = {}
    for item in all_tags:
        if item in ocorrencia:
            ocorrencia[item] += 1
        else:
            ocorrencia[item] = 1
    print(ocorrencia)
    return render_template('dashboards/index.html', ocorrencia=ocorrencia)


@app.route('/criar_tag', methods=['POST', 'GET'])
def criar_tag():
    if request.method == 'POST':
        nome_tag = request.form['tag'].upper()
        tag_existente = Tag.query.filter_by(nome_tag=nome_tag).first()

        if not tag_existente:
            nova_tag = Tag(nome_tag=nome_tag)
            db.session.add(nova_tag)
            db.session.commit()
            flash('Tag criada com suceso', category='success')
            return redirect(url_for('criar_tag'))
        else:
            flash('Tag existente, você não pode duplicar tag!', category='danger')
            return redirect(url_for('criar_tag'))
    nome_tag = Tag.query.all()
    
    return render_template('dashboards/criar_tag.html', nome_tag=nome_tag)

 

@app.route('/detalhe_sobre/<int:problema_id>')
def recuperar_pro(problema_id):
    problema = Problema.query.get(problema_id)
  
    if problema:
        print(problema.titulo)
        solucao = problema.solucao
        return render_template('registrados/detalhe_problema.html', problema=problema, solucao=solucao )
    else:
        return render_template('404/not_found.html')


@app.route('/atualizar/<int:id>', methods=['GET', 'POST'])
def atualizar_ticket(id):  
    tags_existentes = Tag.query.all()
    problema = Problema.query.get(id)
    if request.method == 'POST':
        problema.titulo = request.form['titulo']
        problema.descricao = request.form['descricao']
        problema.escritor = request.form['escritor']

        if not problema.solucao:
            problema.solucao = Solucao(descricao_solucao=request.form['solucao'])
        else:
            problema.solucao.descricao_solucao = request.form['solucao']

        try:
           db.session.commit()
           flash(f'Ticket {id} atualizado com sucesso :)', category='success')

        except SQLAlchemyError as e:
            db.session.rollback()
            flash('Erro ao atualizar', category='danger')
        
    return render_template('registrados/pagina_editar.html', problema=problema, problema_id=id,  tags_existentes=tags_existentes)
