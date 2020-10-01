import pytest
import requests

from models.user import UserModel
from resources.planPolicy import PlanPolicyResource


# test user
def test_post_user():
    # if requests.get()
    # requests.post("http://localhost:8080/api/planPolicy",data={
    #         "name":"gold",
    #         "desc":"{'acomodação':1,'abrangencia':'nacional'}"
    #         })

    response = requests.post(
        "http://localhost:8080/api/user",
        data={
            "first_name":"Anderson",
            "last_name":"kan",
            "cpf":"460.661.877-66",
            "tel":"(11)4616-4117",
            "cel":"(11)97553-9825",
            "email":"132anderson123@gmail.com",
            "password":"securedisk@2020",
            "type_user":"insured",
            "policy":{
                    "number":"00000000001",
                    "plan_policy_id":1
                    }
	            }
)
    assert response.status_code == 201


def test_get_user():
    response = requests.get("http://localhost:8080/api/user")
    assert response.status_code == 200


def test_put_user():
    response = requests.put(
        "http://localhost:8080/api/user/1",
        data={
            "first_name": "testado",
            "email": "jdfsklj@nxncx"
        })
    assert response.status_code == 200


# test destroy
def test_destroy():
    try:
        user_response = requests.delete(f"http://localhost:8080/api/user/1")
    except Exception as e:
        print(e)
    assert user_response.status_code == 204
