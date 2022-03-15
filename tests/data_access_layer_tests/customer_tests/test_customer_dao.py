# Test create and Delete
from data_access_layer.customer_dao_access.customer_dao_imp import CustomerDAOImp
from entity.customer_entity import Customer

customer_dao = CustomerDAOImp()


def test_create_customer_success():
    test_customer = Customer(0, "Test", "Customer")
    returned_customer = customer_dao.insert_into_customers_table(test_customer)
    # assert returned_customer.customer_id != test_customer.customer_id
    assert returned_customer.customer_id != 0
    print(customer_dao)


def test_create_customer_with_unique_id():
    test_customer_unique = Customer(0, "test", "unique_id")
    result = customer_dao.insert_into_customers_table(test_customer_unique)
    assert result.customer_id != 1


def test_delete_customer_success():
    result = customer_dao.delete_from_customers_table_by_customer_id(-1)
    assert result
