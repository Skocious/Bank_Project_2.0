from data_access_layer.customer_dao_access.customer_dao_imp import CustomerDAOImp
from entity.customer_entity import Customer
from service_layer.customer_service_layer.customer_service_imp import CustomerServiceImp
from utils.custom_exceptions.bad_name import BadName

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)


def test_catch_non_string_first_name():
    try:
        customer_service.create_customer_service(Customer(0, 0, "LN"))
        assert False
    except BadName as e:
        assert str(e) == "Please enter valid first name."


def test_catch_first_name_too_long():
    try:
        customer_service.create_customer_service(Customer(0, "This name is way to long!", "Doe"))
        assert False
    except BadName as e:
        assert str(e) == "Please enter valid first name <20 characters."


def test_catch_last_name_too_long():
    try:
        customer_service.create_customer_service(Customer(0, "Doe", "This name is way to long!"))
        assert False
    except BadName as e:
        assert str(e) == "Please enter valid last name <20 characters."
