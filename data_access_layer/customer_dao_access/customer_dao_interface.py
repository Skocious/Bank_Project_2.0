from abc import ABC, abstractmethod

from entity.customer_entity import Customer


class CustomerDAOInterface(ABC):

    @abstractmethod
    def insert_into_customers_table(self, customer_id) -> Customer:
        pass

    @abstractmethod
    def delete_from_customers_table_by_customer_id(self, customer_id):
        pass

# Create Customer - users can join the bank

# Delete Customer - users can leave the bank
