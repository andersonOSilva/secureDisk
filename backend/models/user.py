from models import db


class UserModel(db.Model):
    __tablename__ = 'user'

    id: int = db.Column(db.Integer, primary_key=True)
    email: str = db.Column(db.String(128), nullable=False, unique=True)
    password: str = db.Column(db.String(256), nullable=False)
    status: str = db.Column(db.String(100), nullable=False, default='ativo')
    type_user: str = db.Column(db.String(100), nullable=False)
    created_date = db.Column(db.Date)

    @staticmethod
    def get_by_email(email):
        return UserModel.query.filter_by(email=email).first()

    @staticmethod
    def get_by_id( id_user: int):
        return UserModel.query.filter_by(id=id_user).first()

    @staticmethod
    def get_by_ids( ids_user):
        return UserModel.query.filter(UserModel.id.in_(ids_user)).all()

    @staticmethod
    def list_all():
        return UserModel.query.order_by(UserModel.email).all()
    
    @staticmethod
    def get_by_status( status):
        return UserModel.query.filter_by(status=status).all()

    @staticmethod
    def authenticate(email, password):
        user = UserModel.query.filter_by(email=email).first()
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
