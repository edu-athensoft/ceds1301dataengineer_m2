import pymysql
from chapter_2_3_4_stream.util import logging_util

# Create a log object to generate log information
logger = logging_util.init_logger('mysql')


class MysqlUtil(object):
    """
    Define MysqlUtil tool class
    """

    def __init__(self, host, user, password, port=3306, charset='utf8', autocommit=False):
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            charset=charset,
            autocommit=autocommit
        )
        logger.info(f'The MySQL database with host {host}:{port} has been connected successfully!')

    def select_db(self, db_name):
        """
        Switch Database
        :param db_name:
        :return:
        """
        self.conn.select_db(db_name)

    def execute(self, sql):
        """
        Execute non-query SQL
        :param sql:
        :return:
        """
        cursor = self.conn.cursor()
        cursor.execute(sql)
        # Determine whether the transaction is automatically committed
        # True: automatic submission, False: non-automatic submission
        if not self.conn.get_autocommit():
            self.conn.commit()
        cursor.close()
        logger.info(f'Non-query SQL statement: {sql} executed successfully')

    def query(self, sql):
        """
        Execute query SQL
        :param sql:
        :return:
        """
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        logger.info(f'Query SQL statement: {sql} executed successfully')
        return result

    def begin_transaction(self):
        """
        Open transaction
        :return:
        """
        # Perform a judgment operation to determine whether the MySQL system has enabled automatic submission
        if self.conn.get_autocommit():
            # If the MySQL side opens the transaction by default, there will be a transaction operation conflict.
            # Turn off the automatic commit manually.
            logger.info('MySQL has turned on automatic transaction submission. To avoid conflicts, turn off automatic '
                        'submission manually.')
            self.conn.autocommit(False)
        # Manually start transaction operation
        self.conn.begin()
        logger.info('Open transaction operation successful')

    def commit_transaction(self):
        """
        Committing a transaction
        :return:
        """
        self.conn.commit()
        logger.info('The transaction is executed successfully, commit the transaction')

    def rollback_transaction(self):
        """
        Rollback Transaction
        :return:
        """
        self.conn.rollback()
        logger.info('Transaction execution failed, rollback transaction')

    def check_table_exists(self, db_name, tb_name):
        """
        Checks whether the data table exists. If it exists, it returns True; if it does not exist, it returns False
        :param db_name: Database name
        :param tb_name: Table name
        :return:
        """
        # Switch Database
        self.select_db(db_name)
        # Define SQL statement, show tables to view all data table information
        sql = "show tables;"
        # Execute SQL query, call its own query method and pass in the tables.sql parameter
        result = self.query(sql)
        # Determine whether tb_name exists in the above query results and return a Boolean value
        return (tb_name,) in result

    def check_table_exists_and_create(self, db_name, tb_name, tb_cols):  # create table T(id int, name varchar(20))
        """
        Check if the data table exists, and if it does not exist, create it automatically
        :param db_name:
        :param tb_name:
        :param tb_cols:
        :return:
        """
        if not self.check_table_exists(db_name, tb_name):
            sql = f'create table {tb_name}({tb_cols}) engine=innodb default charset=utf8;'
            self.execute(sql)
            logger.info(f'{tb_name} has been created successfully in database {db_name}')
        else:
            logger.info(f'{tb_name} already exists in database {db_name}, skip creation')

    def query_with_limit(self, db_name, tb_name, limit=None):
        """
        Perform a full table query on a data table
        :param db_name:
        :param tb_name:
        :param limit:
        :return:
        """
        self.select_db(db_name)
        sql = f"select * from {tb_name}"
        if limit is not None:
            sql += f' limit {limit}'  # select * from T limit 5
        result = self.query(sql)
        logger.info(f'SQL query statement: {sql} executed successfully')
        return result

    def insert_sql(self, sql):
        """
        Execute SQL insert operation
        :param sql:
        :return:
        """
        try:
            self.execute(sql)
        except Exception as e:
            logger.error(f'{sql} Insert statement execution exception, error message: {e}')
            raise e
        else:
            logger.info(f'{sql} Insert statement executed successfully without any exception')

    def insert_sql_without_commit(self, sql):
        """
        Execute SQL insert operation without transaction
        :param sql:
        :return:
        """
        try:
            self.conn.cursor().execute(sql)
        except Exception as e:
            logger.warning(f'tables.sql is : {sql}')
            logger.error(f'{sql} Insert statement execution exception, error message: {e}')
            raise e
        logger.info(f'{sql} Insert statement executed successfully without any exception')

    def close(self):
        """
        Close the connection object
        :return:
        """
        if self.conn:
            self.conn.close()
        logger.info('conn connection object closed successfully')


def get_mysql_util(host, user, password, port=3306, charset='utf8', autocommit=False):
    """
    Get the mysqlutil database object
    :param host:
    :param user:
    :param password:
    :param port:
    :param charset:
    :param autocommit:
    :return:
    """
    mysqlutil = MysqlUtil(host, user, password, port, charset, autocommit)
    return mysqlutil


def get_processed_files(util: MysqlUtil, db_name, tb_name, tb_cols):
    """
    Get the list of files that have been processed in the metadata database table
    :param util: The parameter representing util must be a MysqlUtil class object
    :param db_name: Metabase Name
    :param tb_name: Metadatabase table name
    :param tb_cols: The fields corresponding to the tables in the metadata table need to be automatically created and changed if the data table itself does not exist
    :return: a list of files that have been processed
    """
    new_list = []
    # Determine whether the metadata table exists. If it does not exist, the table will be automatically created.
    util.check_table_exists_and_create(
        db_name=db_name,
        tb_name=tb_name,
        tb_cols=tb_cols
    )
    results = util.query_with_limit(db_name, tb_name)

    for result in results:
        new_list.append(result[1])

    return new_list
