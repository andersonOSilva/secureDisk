    # numero
	# idplanoapolice


from models import db


class PlanPolicyModel(db.Model):
    __tablename__ = 'planPolicy'

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(30), nullable=False)
    desc: str = db.Column(db.String(30), nullable=False)
    
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'),nullable=False)

    @staticmethod
    def get_by_name(name):
        return db.session.query(PlanPolicy).filter_by(name=name).first()

    @staticmethod
    def get_by_id(id_plan: int):
        return PlanPolicy.query.filter_by(id=id_plan).first()

    @staticmethod
    def get_by_ids(ids_plan):
        return PlanPolicy.query(PlanPolicy.id.in_(ids_plan)).all()
        
    @staticmethod
    def list_all():
        return PlanPolicy.query.order_by(PlanPolicy.first_name).all()

    def save(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
