from models import db


class PolicyModel(db.Model):
    __tablename__ = 'policy'

    id: int = db.Column(db.Integer, primary_key=True)
    number: str = db.Column(db.String(11), nullable=False, unique=True, autoincrement=True)
    status: str = db.Column(db.String(100), nullable=False, default='ativo')
    created_date = db.Column(db.Date)

    plan_policy_id = db.Column(db.Integer, db.ForeignKey('planPolicy.id', ondelete='CASCADE', onupdate='CASCADE'))
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'),nullable=False)

    @staticmethod
    def get_by_number(number):
        return PolicyModel.query.filter_by(number=number).first()

    @staticmethod
    def get_by_id(id_policy: int):
        return PolicyModel.query.filter_by(id=id_policy).first()

    @staticmethod
    def get_by_ids(ids_policy):
        return PolicyModel.query(PolicyModel.id.in_(ids_policy)).all()
    
    @staticmethod
    def get_by_plan_policy_id(plan_policy_id):
        return PolicyModel.query.filter_by(plan_policy_id=plan_policy_id).first()
        
    @staticmethod
    def list_all():
        return PolicyModel.query.order_by(PolicyModel.number).all()
    
    @staticmethod
    def get_by_status( status):
        return PolicyModel.query.filter_by(status=status).all()

    def save(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
