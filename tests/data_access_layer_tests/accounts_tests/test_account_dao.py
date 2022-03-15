from data_access_layer.account_dao_access.account_dao_implementation import AccountDAOImp
from entity.account_entity import Account
from service_layer.account_service_layer.account_service_imp import AccountServiceImp
from utils.custom_exceptions.id_not_found import IdNotFound

account_dao = AccountDAOImp()
account_service = AccountServiceImp(account_dao)


def test_create_new_account():
    test_account = Account(1000, 100, 0)
    returned_account = account_dao.create_new_account(test_account)
    assert returned_account.account_id == test_account.account_id


def test_non_int_id():
    try:
        account = Account("zero", -2, -2)
        result = account_dao.create_new_account(account)
        assert result.account_id != 0
    except IdNotFound as e:
        assert str(e) == "Id not found"


def test_get_account_info_by_id():
    test_account2 = Account(2000, 100, 0)
    created_account = account_dao.create_new_account(test_account2)
    new_acct_get = account_dao.get_account_info_by_account_id(6)
    assert new_acct_get.account_id != created_account.account_id


def test_no_account_found_by_id():
    try:
        test_account = Account(0, 1, -100)
        result = account_dao.create_new_account(test_account)
        new_result = account_dao.get_account_info_by_account_id(9)
        assert new_result.account_id != result.account_id
    except IdNotFound as e:
        assert str(e) == "Id not found"


def test_get_all_accounts_for_customer():
    get_acct = account_dao.get_all_accounts_for_customer()
    assert len(get_acct) >= 2


def test_get_all_accounts_by_customer_id_no_accounts():
    pass


def test_update_account_by_id():
    update_acct = Account(1000, 100, -1)
    update_acct = account_dao.update_to_account(update_acct)
    result = account_dao.get_account_info_by_account_id(-1)
    assert update_acct.account_bal == result.account_bal


def test_transfer_between_accounts():
    transfer_from = Account(100, 200, 0)
    transfer_to = Account(100, 300, 0)
    account_dao.create_new_account(transfer_from)
    account_dao.create_new_account(transfer_to)


def test_delete_account_by_id():
    deleted_acct = account_dao.delete_account_by_id(-1)
    assert deleted_acct


def test_delete_account_by_id_non_exist():
    try:
        new_result = account_dao.get_account_info_by_account_id(1000)
        assert new_result.account_id != new_result.account_id
    except IdNotFound as e:
        assert str(e) == "Id not found"
