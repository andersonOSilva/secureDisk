    # numero
	# idplanoapolice


from models import db


class PlanProposalModel(db.Model):
    __tablename__ = 'planProposal'

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(30), nullable=False)
    desc: str = db.Column(db.String(30), nullable=False)
    
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'),nullable=False)

    @staticmethod
    def get_by_name(name):
        return db.session.query(PlanProposal).filter_by(name=name).first()

    @staticmethod
    def get_by_id(id_plan: int):
        return PlanProposal.query.filter_by(id=id_plan).first()

    @staticmethod
    def get_by_ids(ids_plan):
        return PlanProposal.query(PlanProposal.id.in_(ids_plan)).all()
        
    @staticmethod
    def list_all():
        return PlanProposal.query.order_by(PlanProposal.first_name).all()

    def save(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
