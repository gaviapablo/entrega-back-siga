from ..extensions import db

class Nota(db.Model):
    __tablename__ = 'nota'
    id = db.Column(db.Integer,primary_key=True)
    valor = db.Column(db.Integer)
    
    boletim_id = db.Column(db.Integer, db.ForeignKey('boletim.id'))

    aluno = db.relationship("Aluno", back_populates="boletim")

    materia_id = db.Column(db.Integer, db.ForeignKey('materia.id'))
    materia = db.relationship("Materia", backref="nota")