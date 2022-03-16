from flask import Flask, request, jsonify
from psycopg import OperationalError

from data_access_layer.account_dao_access.account_dao_implementation import AccountDAOImp
from data_access_layer.customer_dao_access.customer_dao_imp import CustomerDAOImp
from entity.account_entity import Account
from entity.customer_entity import Customer
from service_layer.account_service_layer.account_service_imp import AccountServiceImp
from service_layer.customer_service_layer.customer_service_imp import CustomerServiceImp
from utils.custom_exceptions.bad_id import BadId
from utils.custom_exceptions.bad_name import BadName
from utils.custom_exceptions.id_not_found import IdNotFound

app: Flask = Flask(__name__)

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)
account_dao = AccountDAOImp()
account_service = AccountServiceImp(account_dao)


@app.route("/customer", methods=["POST"])
def create_customer():
    try:
        print("I am here")
        customer_info = request.get_json()
        customer = Customer(customer_info["customerId"],
                            customer_info["firstName"],
                            customer_info["lastName"])
        customer_result = customer_service.create_customer_service(customer)
        customer_as_dict = customer_result.customer_dictionary()
        customer_as_json = jsonify(customer_as_dict)
        return customer_as_json, 201
    except BadName as e:
        return_message = {"message": str(e)}
        return jsonify(return_message)
    except IdNotFound as e:
        return_message = {"message": str(e)}
        return jsonify(return_message)
    except OperationalError as e:
        print(str(e))


@app.route("/customer/<customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    try:
        result = customer_service.delete_customer_service(customer_id)
        result_dictionary = {"result": result}
        result_json = jsonify(result_dictionary)
        return result_json
    except BadId as e:
        return_message = {"message": str(e)}
        return jsonify(return_message)
    except OperationalError as e:
        print(str(e))


@app.route("/accounts", methods=["POST"])
def create_new_account():
    try:
        account_info = request.get_json()
        account = Account(account_info["accountBal"],
                          account_info["customerId"],
                          account_info["accountId"])
        accounts = account_service.service_create_new_account(account)
        accounts_to_dict = accounts.account_dict()
        return jsonify(accounts_to_dict), 200
    except BadId as e:
        return_message = {"message": str(e)}
        return jsonify(return_message)
    except OperationalError as e:
        print(str(e))


@app.route("/accounts/<account_id>", methods=["GET"])
def get_account_by_acct_id(account_id):
    try:
        result = account_service.service_get_account_info_by_account_id(account_id)
        result_dictionary = result.account_dict()
        result_json = jsonify(result_dictionary)
        return result_json
    except BadId as e:
        return_message = {"message": str(e)}
        return jsonify(return_message)
    except OperationalError as e:
        print(str(e))


@app.route("/accounts/<account_id>", methods=["DELETE"])
def delete_account_by_account_id(account_id):
    try:
        result = account_service.service_delete_account_by_id(account_id)
        result_dictionary = {"result": result}
        result_json = jsonify(result_dictionary)
        return result_json
    except BadId as e:
        return_message = {"message": str(e)}
        return jsonify(return_message)
    except OperationalError as e:
        print(str(e))


app.run(host='0.0.0.0', debug=True)
# app.run()
