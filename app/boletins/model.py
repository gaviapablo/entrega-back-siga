from ..extensions import db

class Boletim(db.Model):
    __tablename__ = 'boletim'
    id = db.Column(db.Integer,primary_key=True)

    
    aluno_id = db.Column(db.Integer,db.ForeignKey('aluno.id'))
    aluno = db.relationship("Aluno", back_populates="boletim")

    notas = db.relationship("Nota",backref='boletim_id')