    # numero
	# idplanoapolice


from models import db


class PolicyModel(db.Model):
    __tablename__ = 'policy'

    id: int = db.Column(db.Integer, primary_key=True)
    number: str = db.Column(db.String(30), nullable=False)
    
    plan_policy_id = db.Column(db.Integer, db.ForeignKey('planPolicy.id', ondelete='CASCADE', onupdate='CASCADE'))
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'),nullable=False)

    @staticmethod
    def get_by_number(number):
        return db.session.query(PolicyModel).filter_by(number=number).first()

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
        return PolicyModel.query.order_by(PolicyModel.first_name).all()

    def save(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
