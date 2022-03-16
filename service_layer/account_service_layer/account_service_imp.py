from typing import List

from data_access_layer.account_dao_access.account_dao_implementation import account_dao
from entity.account_entity import Account
from service_layer.account_service_layer.account_service_interface import AccountServiceInterface
from utils.custom_exceptions.account_info_error import AccountInfoError
from utils.custom_exceptions.id_not_found import IdNotFound
from utils.custom_exceptions.no_negative_num import NoNegativeNum


class AccountServiceImp(AccountServiceInterface):

    def service_create_new_account(self, account) -> Account:
        try:
            if type(account.customer_id) != int:
                raise AccountInfoError("Please enter valid customer ID.")
            elif account.account_bal <= 0:
                raise NoNegativeNum("You can not input negative numbers!")
            return self.account_dao.create_new_account(account)
        except KeyError:
            raise IdNotFound("Customer Id not found.")

    def service_get_account_info_by_account_id(self, account_id: int) -> Account:
        return self.account_dao.get_account_info_by_account_id(account_id)

    def service_get_all_accounts_for_customer(self, customer_id: int) -> List[Account]:
        return self.account_dao.get_all_accounts_for_customer(customer_id)

    def service_update_to_account(self, account: Account) -> Account:
        #   try:
        #      if
        #     return self.account_dao.update_to_account(account)
        pass

    def service_delete_account_by_id(self, account_id: int) -> bool:
        try:
            results = self.account_dao.delete_account_by_id(account_id)
            return results
        except KeyError:
            raise IdNotFound(f"Account with the id of {account_id} could not be found")

    def withdraw(self, client_id: int, account_id: int, withdraw: int):
        pass

    # try:
    # result = self.account_dao.get_account_info_by_account_id(account_id)

    def deposit(self, client_id: int, account_id: int, deposit: int):
        pass

    def transfer_money(self, client_id: int, from_id: int, to_id: int, amount: int):
        pass
