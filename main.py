from flask import Flask, request, jsonify

from data_access_layer.customer_dao_access.customer_dao_imp import CustomerDAOImp
from entity.customer_entity import Customer
from service_layer.customer_service_layer.customer_service_imp import CustomerServiceImp

app: Flask = Flask(__name__)

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)


@app.route("/customer", methods=["POST"])
def create_customer():
    customer_info_as_dict = request.get_json()
    customer = Customer(customer_info_as_dict["customerId"], customer_info_as_dict["firstName"],
                        customer_info_as_dict["lastName"])
    customer_result = customer_service.create_customer_service(customer)
    customer_as_dict = customer_result.customer_dictionary()
    customer_as_json = jsonify(customer_as_dict)
    return customer_as_json

"""
@app.route("/customer/<customer_id>", methods=["DELETE"])
def get_customer_with_unique_id(customer_id: str):
    result: Customer = customer_service.delete_customer_service(customer_id)
    result_dictionary = {"result": result}
    result_json = jsonify(result_dictionary)
    return result_json
"""

app.run()
