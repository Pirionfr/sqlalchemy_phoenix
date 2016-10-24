from sqlalchemy import types as sqltypes
from sqlalchemy.types import INTEGER, BIGINT, SMALLINT, VARCHAR, CHAR, \
    FLOAT, DATE, BOOLEAN, DECIMAL, TIMESTAMP, TIME, VARBINARY

class TINYINT(sqltypes.Integer):
    __visit_name__ = "INTEGER"

class UTINYINT(sqltypes.Integer):
    __visit_name__ = "INTEGER"

class UINTEGER(sqltypes.Integer):
    __visit_name__ = "INTEGER"

class DOUBLE(sqltypes.BIGINT):
    __visit_name__ = "BIGINT"

class DOUBLE(sqltypes.BIGINT):
    __visit_name__ = "BIGINT"

class UDOUBLE(sqltypes.BIGINT):
    __visit_name__ = "BIGINT"

class UFLOAT(sqltypes.FLOAT):
    __visit_name__ = "FLOAT"

class ULONG(sqltypes.BIGINT):
    __visit_name__ = "BIGINT"

class UTIME(sqltypes.TIME):
    __visit_name__ = "TIME"


class UDATE(sqltypes.DATE):
    __visit_name__ = "DATE"

class UTIMESTAMP(sqltypes.TIMESTAMP):
    __visit_name__ = "TIMESTAMP"

class ROWID (sqltypes.String):
    __visit_name__ = "VARCHAR"

COLUMN_DATA_TYPE ={
    -6: TINYINT,
    -5: BIGINT,
    -3: VARBINARY,
    1: CHAR,
    3: DECIMAL,
    4: INTEGER,
    5: SMALLINT,
    6: FLOAT,
    8: DOUBLE,
    9: UINTEGER,
    10: ULONG,
    11: UTINYINT,
    12: VARCHAR,
    13: ROWID,
    14: UFLOAT,
    15: UDOUBLE,
    16: BOOLEAN,
    18: UTIME,
    19: UDATE,
    20: UTIMESTAMP,
    91: DATE,
    92: TIME,
    93: TIMESTAMP
}