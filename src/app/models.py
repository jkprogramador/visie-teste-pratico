from app import db

class Pessoa(db.Model):
    __tablename__ = 'pessoas'
    id = db.Column('id_pessoa', db.SmallInteger, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    rg = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    data_admissao = db.Column(db.Date, nullable=False)
    funcao = db.Column(db.String(100), nullable=True)

    @property
    def data(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'rg': self.rg,
            'cpf': self.cpf,
            'data_nascimento': self.data_nascimento.strftime('%Y-%m-%d'),
            'data_admissao': self.data_admissao.strftime('%Y-%m-%d'),
            'data_admissao_locale': self.data_admissao.strftime('%d/%m/%Y'),
            'funcao': self.funcao,
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()