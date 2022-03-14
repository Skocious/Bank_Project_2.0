from flask import Flask, request, jsonify
from data_access_layer.account_dao_access.account_dao_implementation import AccountDAOImp
from entity.account_entity import Account

app: Flask = Flask(__name__)

account_dao = AccountDAOImp()


@app.route("/account", methods=["POST"])
def test_create_new_account():
    test_account = Account(1000, 1, 0)
    returned_account = account_dao.create_new_account(test_account)
    assert returned_account.account_id == test_account.account_id


def test_get_account_info_by_id():
    test_account2 = Account(2000, 1, 0)
    created_account = account_dao.create_new_account(test_account2)
    new_acct_get = account_dao.get_account_info_by_account_id(2)
    assert new_acct_get.account_id != created_account.account_id


def test_get_all_accounts_for_customer():
    get_acct = account_dao.get_all_accounts_for_customer()
    assert len(get_acct) >= 2


def test_update_account_by_id():
    update_acct = Account(1000, 2, 2)
    update_acct = account_dao.update_to_account(update_acct)
    result = account_dao.get_account_info_by_account_id(2)
    assert update_acct.account_bal == result.account_bal


def test_delete_account_by_id():
    deleted_acct = account_dao.delete_account_by_id(-1)
    assert deleted_acct
