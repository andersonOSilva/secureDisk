from models import db


class InsuredModel(db.Model):
    __tablename__ = 'insured'

    id: int = db.Column(db.Integer, primary_key=True)
    first_name: str = db.Column(db.String(30), nullable=False)
    last_name: str = db.Column(db.String(100), nullable=False)
    cpf: str = db.Column(db.String(14), nullable=False, unique=True)
    tel: str = db.Column(db.String(10), nullable=False)
    cel: str = db.Column(db.String(11), nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'),nullable=False)

    @staticmethod
    def get_by_email(email):
        return db.session.query(InsuredModel).filter_by(email=email).first()

    @staticmethod
    def get_by_id(id_insured: int):
        return InsuredModel.query.filter_by(id=id_insured).first()

    @staticmethod
    def get_by_ids(ids_insured):
        return InsuredModel.query(InsuredModel.id.in_(ids_insured)).all()
    
    @staticmethod
    def get_by_user_id(user_id):
        return InsuredModel.query.filter_by(user_id=user_id).first()
        

    @staticmethod
    def get_cpf(cpf):
        return InsuredModel.query.get(cpf=cpf)


    @staticmethod
    def list_all():
        return InsuredModel.query.order_by(InsuredModel.first_name).all()

    def save(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
