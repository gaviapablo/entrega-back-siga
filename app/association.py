from .extensions import db

association_table = db.Table('association',db.Model.metadata,
                    db.Column('materia_id', db.Integer,db.ForeignKey('materia.id')),
                    db.Column('aluno_id', db.Integer,db.ForeignKey('aluno.id')))

