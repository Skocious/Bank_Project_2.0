from abc import ABC, abstractmethod
from typing import List

from entity.account_entity import Account

"""customers can:
 - create account
 - deposit money
 - withdraw money
 - view account
 - view all accounts
 - delete account - with no money in it
 - transfer money between accounts
 """


class AccountDAOInterface(ABC):

    @abstractmethod
    def create_new_account(self, account: Account) -> Account:
        pass

    @abstractmethod
    def get_account_info_by_account_id(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def get_all_accounts_for_customer(self) -> List[Account]:
        pass

    @abstractmethod
    def update_to_account(self, account: Account) -> Account:
        pass

    @abstractmethod
    def delete_account_by_id(self, account_id: int) -> bool:
        pass
