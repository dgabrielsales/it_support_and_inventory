from flask import render_template, request, redirect, url_for, flash, session , jsonify
from app import app, db
from sqlalchemy.exc import SQLAlchemyError
from models import Problema, Solucao, Tag, Equipamento, Setor, Alocacao



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


@app.route('/base_conhecimento', methods=['GET'])
def problemas_cadastrados():
    problemas = Problema.query.all()
    ids_problemas = [problema.id for problema in problemas]
    print(ids_problemas)
    return render_template('registrados/problemas_cadastrados.html', problemas=problemas, ids_problemas=ids_problemas)



@app.route('/dashboard')
def dash():
    problemas = Problema.query.all()
    contagem_tags = {}
    for problema in problemas:
        for tag in problema.tags:
            if tag.nome_tag in contagem_tags:
                contagem_tags[tag.nome_tag] += 1
            else:
                contagem_tags[tag.nome_tag] = 1
    
    dados_grafico = [['Tags', 'Quantidade']]
    for tag, qtd in contagem_tags.items():
        dados_grafico.append([tag, qtd])
    return render_template('dashboards/index.html', dados_grafico=dados_grafico)
    


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
        return redirect(url_for('index'))

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

@app.route('/invetario', methods=['GET'])
def inventario():
   # ativos = .query.all()
    print()
    return render_template('./inventario/inventario.html')

##condicional teste
@app.route('/cadastrar_ativo', methods=['GET'])
def cadastro_ativo():
    return render_template('./inventario/inserir_ativo.html')

@app.route('/enviar_ativo', methods=['GET', 'POST'])
def inserir_ativo():
    if request.method == 'POST':
        nome_ativo = request.form['nome_ativo']
        data_compra = request.form['data_compra']
        numero_serie = request.form['numero_serie']
        marca = request.form['marca']
        dados_ativos = Equipamento(nome_produto=nome_ativo,   data_compra=data_compra, numero_serie=numero_serie, marca=marca)
        db.session.add(dados_ativos)
        db.session.commit()
        flash(f'Ativo Cadastrado com sucesso :)', category='success')
    return render_template('./inventario/inserir_ativo.html')