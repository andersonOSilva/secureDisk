from models import db

class EmergencyPetModel(db.Model):
    __tablename__ = 'emergencyPet'

    id: int = db.Column(db.Integer, primary_key=True)
    call_type: str = db.Column(db.String(100), nullable=True)
    call: str = db.Column(db.String(100), nullable=True)
    label: str = db.Column(db.String(100), nullable=True)
    latitude: str = db.Column(db.String(999), nullable=False)
    longitude: str = db.Column(db.String(999), nullable=False)
    

    proposal_id = db.Column(db.Integer, db.ForeignKey('proposal.id', ondelete='CASCADE', onupdate='CASCADE'))
    provider_id = db.Column(db.Integer, db.ForeignKey('provider.id', ondelete='CASCADE', onupdate='CASCADE'),default=0)
    collab_id = db.Column(db.Integer, db.ForeignKey('collaborator.id', ondelete='CASCADE', onupdate='CASCADE'),default=0)
    created_date = db.Column(db.Date)

    @staticmethod
    def get_by_id(id):
        return db.session.query(EmergencyPetModel).filter_by(id=id).first()

    @staticmethod
    def get_by_proposal(proposal_id):
        return db.session.query(EmergencyPetModel).filter_by(proposal_id=proposal_id).first()
    
    @staticmethod
    def get_by_collab(collab_id):
        return db.session.query(EmergencyPetModel).filter_by(collab_id=collab_id).all()
    
    @staticmethod
    def get_by_provider(provider_id):
        return db.session.query(EmergencyPetModel).filter_by(provider_id=provider_id).all()

    @staticmethod
    def list_all():
        return EmergencyPetModel.query.order_by(EmergencyPetModel.id).all()

    def save(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()