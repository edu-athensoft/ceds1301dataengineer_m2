import unittest
from unit_2_3.config import project_config as conf
from unit_2_3.util import mysql_util


class TestMySQLUtil(unittest.TestCase):
    """
    Define a test class
    """
    # Define setUp and tearDown methods
    def setUp(self) -> None:
        self.util = mysql_util.get_mysql_util(host=conf.metadata_host, user=conf.metadata_user, password=conf.metadata_password)
        # Create a database
        self.util.execute('create database if not exists unit_2_3 default charset=utf8;')
        # Create a test data table
        self.util.execute('create table if not exists unit_2_3.students(id int, name varchar(20));')

    def tearDown(self) -> None:
        # Delete the data table created by setUp
        self.util.execute('drop table if exists unit_2_3.students;')
        # Delete the test database created by setUp
        self.util.execute('drop database if exists unit_2_3;')
        # Close the connection object
        self.util.close()

    def test_insert_single_sql(self):
        """
        test method
        :return:
        """
        self.util.insert_sql('insert into unit_2_3.students values (1, "Tom");')
        result = self.util.query_all(db_name='unit_2_3', tb_name='students')  # ((), (), ())
        self.assertEqual((1, 'Tom'), result[0])