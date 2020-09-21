    # numero
	# idplanoapolice


from models import db


class ProposalModel(db.Model):
    __tablename__ = 'proposal'

    id: int = db.Column(db.Integer, primary_key=True)
    number: str = db.Column(db.String(30), nullable=False)
    
    plan_proposal_id = db.Column(db.Integer, db.ForeignKey('planProposal.id', ondelete='CASCADE', onupdate='CASCADE'))
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'),nullable=False)

    @staticmethod
    def get_by_number(number):
        return db.session.query(ProposalModel).filter_by(number=number).first()

    @staticmethod
    def get_by_id(id_proposal: int):
        return ProposalModel.query.filter_by(id=id_proposal).first()

    @staticmethod
    def get_by_ids(ids_proposal):
        return ProposalModel.query(ProposalModel.id.in_(ids_proposal)).all()
    
    @staticmethod
    def get_by_plan_proposal_id(plan_proposal_id):
        return ProposalModel.query.filter_by(plan_proposal_id=plan_proposal_id).first()
        
    @staticmethod
    def list_all():
        return ProposalModel.query.order_by(ProposalModel.first_name).all()

    def save(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
