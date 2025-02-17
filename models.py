from app import db
from datetime import datetime, timezone
import pytz

problema_tag_association = db.Table(
    'problema_tag_association',
    db.Column('problema_id', db.Integer, db.ForeignKey('problema.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

class Problema(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), nullable=False) 
    descricao = db.Column(db.String(200), nullable=False)
    escritor = db.Column(db.String(20))
    tags = db.relationship('Tag', secondary=problema_tag_association, backref='problemas')
    solucao = db.relationship('Solucao', backref='problema', uselist=False, cascade="all, delete")
    data_hora = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(pytz.timezone('America/Sao_Paulo')))

class Tag(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    nome_tag = db.Column(db.String(50))

class Solucao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao_solucao = db.Column(db.String(200), nullable=False)
    problema_id = db.Column(db.Integer, db.ForeignKey('problema.id'), unique=True, nullable=False)

class Equipamento(db.Model):
    id_equipamento = db.Column(db.Integer, primary_key=True)
    nome_produto = db.Column(db.String(70))
    data_compra = db.Column(db.Date())
    numero_serie = db.Column(db.String(20))
    marca = db.Column(db.String(20))

class Alocacao(db.Model):
    id_alocacao = db.Column(db.Integer, primary_key=True)
    id_equipamento = db.Column(db.Integer, db.ForeignKey('equipamento.id_equipamento'), nullable=False)
    id_setor = db.Column(db.Integer, db.ForeignKey('setor.id_setor'),nullable=False)
    data_movimentacao = db.Column(db.Date(),  nullable=False)
    data_retorno = db.Column(db.Date())
    obs = db.Column(db.String(100)) 


class Setor(db.Model):
    id_setor = db.Column(db.Integer, primary_key=True)
    nome_setor = db.Column(db.Text)
