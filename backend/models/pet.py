from models import db

class PetModel(db.Model):
    __tablename__ = 'pet'

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), nullable=False)
    species: str = db.Column(db.String(100), nullable=False)
    breed: str = db.Column(db.String(100), nullable=False)
    size: float = db.Column(db.Float(), nullable=False)
    weight: float = db.Column(db.Float(), nullable=False)
   
    status: str = db.Column(db.String(), nullable=False, default='ativo')

    insured_id = db.Column(db.Integer, db.ForeignKey('insured.id', ondelete='CASCADE', onupdate='CASCADE'))
    created_date = db.Column(db.Date)

    @staticmethod
    def get_by_id(id_pet):
        return PetModel.query.filter_by(id=id_pet).first()

    @staticmethod
    def get_by_species(species):
        return db.session.query(PetModel).filter_by(species=species).all()
    
    @staticmethod
    def get_by_breed(breed):
        return db.session.query(PetModel).filter_by(breed=breed).all()
    
    @staticmethod
    def get_by_insured(insured_id):
        return db.session.query(PetModel).filter_by(insured_id=insured_id).all()

    @staticmethod
    def list_all():
        return PetModel.query.order_by(PetModel.insured_id).all()

    def save(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


