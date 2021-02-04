from ..extensions import db

class Turma(db.Model):
    __tablename__ = 'turma'
    id = db.Column(db.Integer,primary_key=True)
    horario = db.Column(db.DateTime)
    
    materia_id = db.Column(db.String(15),nullable=False)
    professor_id = db.Column(db.Integer,db.ForeignKey('professor.id'))