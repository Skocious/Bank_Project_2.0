from utils.create_connection import connection


def db_reset():
    sql = "TRUNCATE TABLE customers, accounts RESTART IDENTITY CASCADE"
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    result = cursor.rowcount
    assert result
    print(result)


def dbc_insert():
    sql = "insert into customers values(-1,'for', 'delete'), (100,'TestA', 'Customer')"
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    result = cursor.rowcount
    assert result
    print(result)


def dba_insert():
    sql = "insert into accounts values(0,100, -1)"
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    result = cursor.rowcount
    assert result
    print(result)


def test_db_reset():
    assert db_reset()


def test_dbc_insert():
    assert dbc_insert()


def test_dba_insert():
    assert dba_insert()

