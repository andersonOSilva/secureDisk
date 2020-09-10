from models import db


class InsuredModel(db.Model):
    __tablename__ = 'insured'

    id: int = db.Column(db.Integer, primary_key=True)
    first_name: str = db.Column(db.String(30), nullable=False)
    last_name: str = db.Column(db.String(100), nullable=False)
    cpf: str = db.Column(db.String(14), nullable=False, unique=True)
    tel: str = db.Column(db.String(10), nullable=False)
    cel: str = db.Column(db.String(11), nullable=False)
    email: str = db.Column(db.String(128), nullable=False, unique=True)
    password: str = db.Column(db.String(256), nullable=True)
    status: str = db.Column(db.String(100), nullable=False, default='ativo')
    created_date = db.Column(db.Date)
    

    @staticmethod
    def get_by_email(email):
        return db.session.query(InsuredModel).filter_by(email=email).first()

    @staticmethod
    def get_by_id(id_user: int):
        return InsuredModel.query.filter_by(id=id_user).first()
    @staticmethod
    def get_cpf(cpf):
        return InsuredModel.query.get(cpf=cpf)
    
    @staticmethod
    def get_status(status):
        return InsuredModel.query.filter_by(status=status).all()

    @staticmethod
    def get_by_ids(ids_user):
        return InsuredModel.query(InsuredModel.id.in_(ids_user)).all()

    @staticmethod
    def list_all():
        return InsuredModel.query.order_by(InsuredModel.first_name).all()

    @staticmethod
    def authenticate(email, password):
        user = InsuredModel.query.filter_by(email=email).first()
        if user and user.status == 'ativo':
            if password == user.password:
                return user
        return None

    def save(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
