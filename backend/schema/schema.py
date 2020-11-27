from models import db
from models.pet import PetModel
from models.user import UserModel
from models.policy import PolicyModel
from models.insured import InsuredModel
from models.provider import ProviderModel
from models.proposal import ProposalModel
# from models.emergency import EmergencyModel
from models.planPolicy import PlanPolicyModel
from models.petSchedule import PetScheduleModel
from models.planProposal import PlanProposalModel


from os import environ
# importar model aqui

from sqlalchemy import create_engine


class Schema:
    @staticmethod
    def migration():
        # aqui alteramos o banco
        engine = create_engine(environ.get('SQLALCHEMY_DATABASE_URI'))
        # <ClassModelName>.__table__.drop(engine)
		#cria tabelas
        db.create_all()
# # ________________________________________________________________________
import sqlite3

def tabela():
	
	conn = sqlite3.connect('securedisk.db')
	c = conn.cursor()

	# Create table
	c.execute('''
		
		''')

	#c.execute("INSERT INTO segurado VALUES ('123','fulano','fulano@gmail.com','123')")

	conn.commit()
	conn.close()