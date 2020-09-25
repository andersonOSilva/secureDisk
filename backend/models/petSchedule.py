    # idprov
	# idproposta
	# data
	# hora
	# desc
from models import db

class PetScheduleModel(db.Model):
    __tablename__ = 'petSchedule'

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), nullable=False)
    email: str = db.Column(db.String(100), nullable=False)
    # date = db.Column(db.Date)
    date:str = db.Column(db.String(10),nullable=False)
    time: str = db.Column(db.String(5), nullable=False)

    status: str = db.Column(db.String(), nullable=False, default='ativo')

    provider_id = db.Column(db.Integer, db.ForeignKey('provider.id', ondelete='CASCADE', onupdate='CASCADE'))
    proposal_id = db.Column(db.Integer, db.ForeignKey('proposal.id', ondelete='CASCADE', onupdate='CASCADE'))
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id', ondelete='CASCADE', onupdate='CASCADE'))
    created_date = db.Column(db.Date)

    @staticmethod
    def get_by_id(id_pet_schedule):
        return db.session.query(PetScheduleModel).filter_by(id=id_pet_schedule).first()

    @staticmethod
    def get_by_name(name):
        return db.session.query(PetScheduleModel).filter_by(name=name).all()
    
    @staticmethod
    def get_by_email(email):
        return db.session.query(PetScheduleModel).filter_by(email=email).all()
    
    @staticmethod
    def get_by_pet(pet_id):
        return db.session.query(PetScheduleModel).filter_by(pet_id=pet_id).all()
    
    @staticmethod
    def get_by_proposal(proposal_id):
        return db.session.query(PetScheduleModel).filter_by(proposal_id=proposal_id).all()
    
    @staticmethod
    def get_by_provider(provider_id):
        return db.session.query(PetScheduleModel).filter_by(provider_id=provider_id).all()
    
    @staticmethod
    def get_by_status(status):
        return db.session.query(PetScheduleModel).filter_by(status=status).all()
    
    @staticmethod
    def get_by_date(date):
        return db.session.query(PetScheduleModel).filter_by(date=date).all()
    
    @staticmethod
    def get_by_hour(time):
        return db.session.query(PetScheduleModel).filter_by(time=time).all()
    
    @staticmethod
    def list_all():
        return PetScheduleModel.query.order_by(PetScheduleModel.name).all()

    def save(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


