import time

def ts13_to_ts10(ts):
    """
    Normalize a 13-digit timestamp to a 10-digit timestamp
    In JSON data, timestamps are in milliseconds
    Timestamps read from JSON need to be converted to seconds (10 digits) to be used by Python
    :param ts:
    :return:
    """
    return ts // 1000


def ts10_to_date_str(ts, format_str='%Y-%m-%d %H:%M:%S'):
    """
    Convert a 10-digit timestamp to a date string
    :param ts:
    :param format_str:
    :return:
    """
    struct_time = time.localtime(ts)
    return time.strftime(format_str, struct_time)


def ts13_to_date_str(ts, format_str='%Y-%m-%d %H:%M:%S'):
    """
    Convert a 13-digit timestamp to a date string
    :param ts:
    :param format_str:
    :return:
    """
    ts = ts13_to_ts10(ts)
    return ts10_to_date_str(ts, format_str)


if __name__ == '__main__':
    print(ts13_to_date_str(1725120000000))