from models import db


class CollaboratorModel(db.Model):
    __tablename__ = 'collaborator'

    id: int = db.Column(db.Integer, primary_key=True)
    first_name: str = db.Column(db.String(30), nullable=False)
    last_name: str = db.Column(db.String(100), nullable=False)
    registration: str = db.Column(db.String(10), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'))
    

    @staticmethod
    def get_by_email(first_name):
        return CollaboratorModel.query.filter_by(first_name=first_name).first()

    @staticmethod
    def get_registration(registration):
        return CollaboratorModel.query.filter_by(registration=registration).first()

    @staticmethod
    def get_by_id(id_collaborator: int):
        return CollaboratorModel.query.filter_by(id=id_collaborator).first()

    @staticmethod
    def get_by_ids(ids_collaborator):
        return CollaboratorModel.query(CollaboratorModel.id.in_(ids_collaborator)).all()
    
    @staticmethod
    def get_by_user_id(user_id):
        return CollaboratorModel.query.filter_by(user_id=user_id).first()

    @staticmethod
    def list_all():
        return CollaboratorModel.query.order_by(CollaboratorModel.first_name).all()

    def save(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
