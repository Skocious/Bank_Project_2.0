from typing import List

from data_access_layer.account_dao_access.account_dao_implementation import account_dao
from entity.account_entity import Account
from service_layer.account_service_layer.account_service_interface import AccountServiceInterface


class AccountServiceImp(AccountServiceInterface):

    def service_create_new_account(self, account: Account) -> Account:
        return account_dao.create_new_account(account)


    def service_get_account_info_by_account_id(self, account_id: int) -> Account:
        pass

    def service_get_all_accounts_for_customer(self) -> List[Account]:
        pass

    def service_update_to_account(self, account: Account) -> Account:
        pass

    def service_delete_account_by_id(self, account_id: int) -> bool:
        pass
