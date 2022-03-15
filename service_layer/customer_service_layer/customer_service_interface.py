from abc import ABC, abstractmethod

from data_access_layer.customer_dao_access.customer_dao_interface import CustomerDAOInterface

from entity.customer_entity import Customer


class CustomerServiceInterface(ABC):

    def __init__(self, customer_dao: CustomerDAOInterface):
        self.customer_dao = customer_dao

    @abstractmethod
    def create_customer_service(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def delete_customer_service(self, customer_id: str) -> bool:
        pass
