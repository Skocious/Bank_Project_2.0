from entity.customer_entity import Customer
from service_layer.customer_service_layer.customer_service_interface import CustomerServiceInterface
from utils.custom_exceptions.bad_id import BadId
from utils.custom_exceptions.bad_name import BadName


class CustomerServiceImp(CustomerServiceInterface):

    def create_customer_service(self, customer: Customer) -> Customer:
        if type(customer.first_name) != str:
            raise BadName("Please enter valid first name.")
        elif len(customer.first_name) >= 21:
            raise BadName("Please enter valid first name <20 characters.")
        elif type(customer.last_name) != str:
            raise BadName("Please enter valid last name.")
        elif len(customer.last_name) >= 21:
            raise BadName("Please enter valid last name <20 characters.")
        return self.customer_dao.insert_into_customers_table(customer)

    def delete_customer_service(self, customer_id: str) -> bool:
        try:
            return self.customer_dao.delete_from_customers_table_by_customer_id(int(customer_id))
        except ValueError:
            raise BadId("Please provide a valid customer Id.")
