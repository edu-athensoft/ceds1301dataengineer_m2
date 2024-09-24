from chapter_5.util import str_util
from chapter_5.config import project_config as conf


def get_metadata_sql(count, batch_commit, model, table_name, table_cols):
    #execution_mode = str_util.check_str_null_and_transform_to_sql_null(model.execution_mode)
    if count % conf.batch_commit == 0:
        sql = f"insert into {table_name}" \
              f" {table_cols} " \
              f"values (" \
              f"'{model.date_ts}', {batch_commit});"
    else:
        sql = f"insert into {table_name}" \
              f" {table_cols} " \
              f"values (" \
              f"'{model.date_ts}', {count % batch_commit});"

    return sql