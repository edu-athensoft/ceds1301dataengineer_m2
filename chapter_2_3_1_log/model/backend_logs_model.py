from chapter_2_3_1_log.config import project_config as conf


class BackendLogsModel(object):
    """
    Log information model class
    """

    def __init__(self, log_data: str):
        """
        Initialization method
        1. Split the log_data data into lists, the separator is \t
        2. Assign each element in the list to the corresponding attribute
        """
        data = log_data.split('\t')

        self.log_time = data[0]
        self.log_level = data[1].strip('[]')
        self.log_module = data[2]
        self.response_time = data[3][14:-2]
        self.province = data[4]
        self.city = data[5]
        self.log_text = data[6]

    def insert_sql(self):
        """
        Generate SQL statement to insert data
        """
        return f'insert into {conf.target_logs_table_name}(' \
               f'log_time, log_level, log_module, response_time, province, city, log_text)' \
               f' values("{self.log_time}",' \
               f'"{self.log_level}",' \
               f'"{self.log_module}",' \
               f'"{self.response_time}",' \
               f'"{self.province}",' \
               f'"{self.city}",' \
               f'"{self.log_text}");'
