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
    solucao = db.relationship('Solucao', backref='problema', uselist=False)
    data_hora = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(pytz.timezone('America/Manaus')))

class Tag(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    nome_tag = db.Column(db.String(50))

class Solucao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao_solucao = db.Column(db.String(200), nullable=False)
    problema_id = db.Column(db.Integer, db.ForeignKey('problema.id'), unique=True, nullable=False)
