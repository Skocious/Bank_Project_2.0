from flask import Flask, request, jsonify
from data_access_layer.customer_dao_access.customer_dao_imp import CustomerDAOImp
from entity.customer_entity import Customer
from service_layer.customer_service_layer.customer_service_imp import CustomerServiceImp
from utils.custom_exceptions.bad_id import BadId
from utils.custom_exceptions.bad_name import BadName
from utils.custom_exceptions.id_not_found import IdNotFound

app: Flask = Flask(__name__)

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)


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


app.run(host='0.0.0.0', debug=True)
#app.run()

