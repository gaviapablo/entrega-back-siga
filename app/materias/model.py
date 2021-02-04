from ..extensions import db
from ..association import association_table

class Materia(db.Model):
    __tablename__ = 'materia'
    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(50),nullable=False)
    codigo = db.Column(db.String(15),nullable=False)
    creditos = db.Column(db.Integer)


    turmas = db.relationship('Turma',backref='materia')
    alunos = db.relationship('Aluno',secondary=association_table,backref='materias')
    nota = db.relationship("Nota", uselist=False, backref="materia")