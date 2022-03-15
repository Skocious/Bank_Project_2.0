"""
sql = ""
cursor = connection.cursor()
cursor.execute(sql, [])
connection.commit()
return
"""

from typing import List
from data_access_layer.account_dao_access.account_dao_interface import AccountDAOInterface
from entity.account_entity import Account
from utils.create_connection import connection

account_dao = AccountDAOInterface


class AccountDAOImp(AccountDAOInterface):

    def create_new_account(self, account: Account) -> Account:
        sql = "insert into accounts values(%s, %s, default) returning account_id"
        cursor = connection.cursor()
        cursor.execute(sql, (account.account_bal, account.customer_id))
        connection.commit()
        result = cursor.fetchone()[0]
        account.account_bal = result
        return account

    def get_account_info_by_account_id(self, account_id: int) -> Account:
        sql = "select * from accounts where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        result = cursor.fetchone()
        account = Account(*result)
        return account

    def get_all_accounts_for_customer(self) -> List[Account]:
        sql = "select * from accounts"
        cursor = connection.cursor()
        cursor.execute(sql)
        accounts = cursor.fetchall()
        account_list = []
        for a in accounts:
            account_list.append(Account(*a))
        return account_list

    def update_to_account(self, account: Account) -> Account:
        sql = "update accounts set account_bal = %s, customer_id = %s where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (account.account_bal, account.customer_id, account.account_id))
        connection.commit()
        return account

    def transfer_funds(self, sender_account_id: int, receiver_id: float):
        pass

    def delete_account_by_id(self, account_id: int) -> bool:
        sql = "delete from accounts where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        connection.commit()
        return True
