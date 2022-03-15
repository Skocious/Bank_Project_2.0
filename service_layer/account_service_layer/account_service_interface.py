from abc import ABC, abstractmethod
from typing import List
from data_access_layer.account_dao_access.account_dao_interface import AccountDAOInterface
from entity.account_entity import Account


class AccountServiceInterface(ABC):

    def __init__(self, account_dao: AccountDAOInterface):
        self.account_dao = account_dao

    @abstractmethod
    def service_create_new_account(self, account: Account) -> Account:
        pass

    @abstractmethod
    def service_get_account_info_by_account_id(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def service_get_all_accounts_for_customer(self) -> List[Account]:
        pass

    @abstractmethod
    def service_update_to_account(self, account: Account) -> Account:
        pass

    @abstractmethod
    def service_delete_account_by_id(self, account_id: int) -> bool:
        pass
