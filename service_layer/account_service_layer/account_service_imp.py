from typing import List

from data_access_layer.account_dao_access.account_dao_implementation import account_dao
from entity.account_entity import Account
from service_layer.account_service_layer.account_service_interface import AccountServiceInterface
from utils.custom_exceptions.id_not_found import IdNotFound


class AccountServiceImp(AccountServiceInterface):

    def service_create_new_account(self, account) -> Account:
        return self.account_dao.create_new_account(account)

    def service_get_account_info_by_account_id(self, account_id: int) -> Account:
        return self.account_dao.get_account_info_by_account_id(account_id)

    def service_get_all_accounts_for_customer(self) -> List[Account]:
        return self.service_get_all_accounts_for_customer()

    def service_update_to_account(self, account: Account) -> Account:
        return self.account_dao.update_to_account(account)

    def service_delete_account_by_id(self, account_id: int) -> bool:
        try:
            results = self.account_dao.delete_account_by_id(account_id)
            return results
        except KeyError:
            raise IdNotFound(f"Account with the id of {account_id} could not be found")