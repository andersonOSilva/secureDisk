from models import db


class ProviderModel(db.Model):
    __tablename__ = 'provider'

    id: int = db.Column(db.Integer, primary_key=True)
    business_name: str = db.Column(db.String(30), nullable=False)
    fantasy_name: str = db.Column(db.String(100), nullable=False)
    cnpj: str = db.Column(db.String(19), nullable=False, unique=True)
    
    address: str = db.Column(db.String(255), nullable=False)
    type_provider: str = db.Column(db.String(256), nullable=False)
    
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'))

    @staticmethod
    def get_by_email(email):
        return ProviderModel.query.filter_by(email=email).first()

    @staticmethod
    def get_cpf(cnpj):
        return ProviderModel.query.filter_by(cnpj=cnpj).first()

    @staticmethod
    def get_by_id(id_provider):
        return ProviderModel.query.filter_by(id=id_provider).first()
        
    @staticmethod
    def get_by_ids(ids_provider):
        return ProviderModel.query(ProviderModel.id.in_(ids_provider)).all()
    
    @staticmethod
    def get_by_user_id(user_id):
        return ProviderModel.query.filter_by(user_id=user_id).first()
    
    @staticmethod
    def list_all():
        return ProviderModel.query.order_by(ProviderModel.fantasy_name).all()

    def save(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
