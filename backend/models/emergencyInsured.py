from models import db

class EmergencyInsuredModel(db.Model):
    __tablename__ = 'emergencyInsured'

    id: int = db.Column(db.Integer, primary_key=True)
    call_type: str = db.Column(db.String(100), nullable=True)
    call: str = db.Column(db.String(100), nullable=True)
    label: str = db.Column(db.String(100), nullable=True)
    latitude: str = db.Column(db.String(999), nullable=False)
    longitude: str = db.Column(db.String(999), nullable=False)
    

    policy_id = db.Column(db.Integer, db.ForeignKey('policy.id', ondelete='CASCADE', onupdate='CASCADE'),nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey('provider.id', ondelete='CASCADE', onupdate='CASCADE'), default=0)
    collab_id = db.Column(db.Integer, db.ForeignKey('collaborator.id', ondelete='CASCADE', onupdate='CASCADE'),default=0)
    created_date = db.Column(db.Date)

    @staticmethod
    def get_by_id(id):
        return db.session.query(EmergencyInsuredModel).filter_by(id=id).first()

    @staticmethod
    def get_by_policy(policy_id):
        return db.session.query(EmergencyInsuredModel).filter_by(policy_id=policy_id).first()
    
    @staticmethod
    def get_by_collab(collab_id):
        return db.session.query(EmergencyInsuredModel).filter_by(collab_id=collab_id).all()
    
    @staticmethod
    def get_by_provider(provider_id):
        return db.session.query(EmergencyInsuredModel).filter_by(provider_id=provider_id).all()

    @staticmethod
    def list_all():
        return EmergencyInsuredModel.query.order_by(EmergencyInsuredModel.id).all()

    def save(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()