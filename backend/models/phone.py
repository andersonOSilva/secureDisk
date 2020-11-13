from models import db


class PhoneModel(db.Model):
    __tablename__ = 'phone'
    
    
    
    id: int = db.Column(db.Integer, primary_key=True)
    phone: str = db.Column(db.String(12), nullable=False, unique=True)
    webphone: str = db.Column(db.String(256), nullable=False)
    branch_line: str = db.Column(db.String(100), nullable=False)
    status: str = db.Column(db.String(100), nullable=False)    
    created_date = db.Column(db.Date)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    @staticmethod
    def get_by_id( id_phone: int):
        return PhoneModel.query.filter_by(id=id_phone).first()
    
    @staticmethod
    def get_by_user_id( id_user):
        return PhoneModel.query.filter_by(user_id=id_user).all()
    
    @staticmethod
    def get_by_ids( ids_user):
        return PhoneModel.query.filter(PhoneModel.id.in_(ids_user)).all()
        
    @staticmethod
    def get_by_branch_line( branch_line):
        return PhoneModel.query.filter_by(branch_line=branch_line).all()
    
    @staticmethod
    def get_by_webphone( webphone):
        return PhoneModel.query.filter_by(webphone=webphone).first()
        
    @staticmethod
    def get_by_phone(phone):
        return PhoneModel.query.filter_by(phone=phone).first()

    @staticmethod
    def get_by_status( status):
        return PhoneModel.query.filter_by(status=status).all()

    @staticmethod
    def list_all():
        return PhoneModel.query.order_by(PhoneModel.created_date).all()
    

    def save(self):
        db.session.merge(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()
