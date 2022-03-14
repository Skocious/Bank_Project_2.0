from abc import ABC, abstractmethod

from data_access_layer.customer_dao_access.customer_dao_interface import CustomerDAOInterface


class CustomerServiceInterface(ABC):

    def __int__(self, customer_dao: CustomerDAOInterface):
        self.customer_dao = customer_dao

    @abstractmethod
    def create_customer_service(self):
        pass

    @abstractmethod
    def get_customer_service(self):
        pass

    @abstractmethod
    def update_customer_service(self):
        pass

    @abstractmethod
    def delete_customer_service(self):
        pass