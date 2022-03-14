from data_access_layer.customer_dao_access.customer_dao_interface import CustomerDAOInterface
from entity.customer_entity import Customer
from utils.create_connection import connection


class CustomerDAOImp(CustomerDAOInterface):

    def insert_into_customers_table(self, customer_object: Customer) -> Customer:
        sql = "insert into customers values(default, %s, %s) returning customer_id"
        cursor = connection.cursor()
        cursor.execute(sql, (customer_object.first_name, customer_object.last_name))
        connection.commit()
        returned_id = cursor.fetchone()[0]
        customer_object.customer_id = returned_id
        return customer_object

    # set upp SQL
    # create cursor
    # use cursor to execute sql a statement
    # remember to commit transaction
    # get teh returned generated id
    # assign to customer object
    # return customer object

    def delete_from_customers_table_by_customer_id(self, customer_id: int) -> bool:
        # create sql query
        # create cursor object
        # use cursor to execute sql
        # ck that the table was affected
        # assuming true, return true
        # else do something else
        sql = "delete from customers where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        connection.commit()
        if cursor.rowcount != 0:
            return True
        else:
            return False


"""
sql = ""
cursor = connection.cursor()
cursor.execute(sql, [])
connection.commit()
return 
"""
# look at cursor commands
