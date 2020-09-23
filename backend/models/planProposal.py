from models import db


class PlanProposalModel(db.Model):
    __tablename__ = 'planProposal'

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(30), nullable=False)
    desc: str = db.Column(db.String(100), nullable=False)
    status: str = db.Column(db.String(100), nullable=False, default='ativo')
    created_date = db.Column(db.Date)
    
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'),nullable=False)

    @staticmethod
    def get_by_name(name):
        return PlanProposalModel.query.filter_by(name=name).first()

    @staticmethod
    def get_by_id(id_plan: int):
        return PlanProposalModel.query.filter_by(id=id_plan).first()

    @staticmethod
    def get_by_ids(ids_plan):
        return PlanProposalModel.query(PlanProposalModel.id.in_(ids_plan)).all()
        
    @staticmethod
    def list_all():
        return PlanProposalModel.query.order_by(PlanProposalModel.name).all()

    @staticmethod
    def get_by_status( status):
        return PlanProposalModel.query.filter_by(status=status).all()

    def save(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
