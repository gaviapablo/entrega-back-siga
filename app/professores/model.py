from ..extensions import db

class Professor(db.Model):
    __tablename__ = 'professor'
    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(50),nullable=False)
    cpf = db.Column(db.Integer,unique=True)
    formação = db.Column(db.Text,nullable=False)

    turmas = db.relationship('Turma',backref='professor')

