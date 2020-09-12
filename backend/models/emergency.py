from models import db

class EmergencyModel(db.Model):
    __tablename__ = 'emergency'

    id: int = db.Column(db.Integer, primary_key=True)
    call_type: str = db.Column(db.String(100), nullable=False)
    call: str = db.Column(db.String(100), nullable=False)
    label: str = db.Column(db.String(100), nullable=False)
    latitude: str = db.Column(db.String(999), nullable=False)
    longitude: str = db.Column(db.String(999), nullable=False)
   
    status: str = db.Column(db.String(), nullable=False, default='ativo')

    insured_id = db.Column(db.Integer, db.ForeignKey('insured.id', ondelete='CASCADE', onupdate='CASCADE'))
    created_date = db.Column(db.Date)

    @staticmethod
    def get_by_id(id_emergency):
        return db.session.query(EmergencyModel).get(id_emergency=id_emergency)

    @staticmethod
    def get_by_type (call_type):
        return db.session.query(EmergencyModel).filter_by(call_type=call_type).all()
    
    @staticmethod
    def get_by_insured(insured_id):
        return db.session.query(EmergencyModel).filter_by(insured_id=insured_id).all()

    def save(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()