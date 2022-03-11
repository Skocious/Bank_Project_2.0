from data_access_layer.customer_dao_access.customer_dao_interface import CustomerDAOInterface
from entity.customer_entity import Customer


class CustomerDAOImp(CustomerDAOInterface):

    def insert_into_customers_table(self, customer_object) -> Customer:
        pass

    def delete_from_customers_table_by_customer_id(self, customer_id: int):
        pass
