"""
String utility methods
"""


def check_null(data):
    """
    Checks whether the passed string is empty, None, or other meaningless content. True means empty, False means not empty
    """
    if not data:
        return True

    data = data.lower()  # data = data.lower() == data ABCD => data.lower() abcd
    if data in ('null', 'none', 'undefined'):
        return True

    return False


def check_null_and_transform(data):
    """
    Check the string. If it is empty, return an empty string. It also has the function of removing the empty characters on both sides of the string.
    """
    if check_null(str(data)):
        return ''
    elif isinstance(data, str):  # 判断左边的变量是否为右边的数据类型 => True or False
        return data.strip()  # strip()：去除字符串两边的空格
    else:
        return data


def check_str_null_and_transform_to_sql_null(data):
    """
    Check the string passed in
    If it is empty, return the 'null' string for SQL insertion
    Otherwise return the data itself and wrap it with "" for SQL insertion
    """
    if check_null(str(data)):
        return 'null'       # insert into T values (null)
    else:
        return f"'{data}'"  # Tom => 'Tom', insert into T values (null, 'Tom')


def check_number_null_and_transform_to_sql_null(data):
    """
    Checks if the passed numeric or string data is empty.
    If it is empty, it returns the string 'null'.
    Otherwise, it returns the data itself.
    """
    if not data or check_null(str(data)):
        return 'null'
    else:
        return data  # 10 => insert into T values (null, 10)


def clear_str(data):
    """
    Handle abnormal characters in strings, such as single quotes, double quotes, commas, semicolons, etc.
    """
    if check_null(data):
        return data

    data = data.replace("'", "")
    data = data.replace("\"", "")
    data = data.replace(";", "")
    data = data.replace(",", "")
    data = data.replace("@", "")
    data = data.replace("\\", "")
    data = data.replace("(", "")
    data = data.replace(")", "")

    return data

