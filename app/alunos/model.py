from ..extensions import db
from ..association import association_table

class Aluno(db.Model):
    __tablename__ = 'aluno'
    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(50),nullable=False)
    dre = db.Column(db.Integer,unique=True)
    cpf = db.Column(db.Integer,unique=True)
    dataNascimento = db.Column(db.String(8),nullable=False)
    sexo = db.Column(db.String(10),nullable=False)
    periodoIngresso = db.Column(db.Integer)
    curso = db.Column(db.String(50),nullable = False)


    materias = db.relationship('Materia',secondary=association_table,backref='alunos')
    boletim = db.relationship("Boletim",uselist=False,backref='aluno')
    