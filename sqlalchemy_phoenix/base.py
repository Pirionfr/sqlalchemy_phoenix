from sqlalchemy.engine.default import DefaultDialect
from sqlalchemy_phoenix.types import COLUMN_DATA_TYPE

from sqlalchemy.sql.compiler import DDLCompiler
from sqlalchemy.exc import CompileError



class PhoenixDDLCompiler(DDLCompiler):

    def visit_primary_key_constraint(self, constraint):
        if constraint.name is None:
            raise CompileError("can't create primary key without a name")
        return DDLCompiler.visit_primary_key_constraint(self, constraint)


class PhoenixDialect(DefaultDialect):
    name = "phoenix"

    ddl_compiler = PhoenixDDLCompiler



    def do_rollback(self, dbapi_conection):
        pass

    def do_commit(self, dbapi_conection):
        pass


    def has_table(self, connection, table_name, schema=None):
        if schema is None:
            query = "SELECT 1 FROM system.catalog WHERE table_name = ? LIMIT 1"
            params = [table_name.upper()]
        else:
            query = "SELECT 1 FROM system.catalog WHERE table_name = ? AND TABLE_SCHEM = ? LIMIT 1"
            params = [table_name.upper(), schema.upper()]
        return connection.execute(query, params).first() is not None


    def get_table_names(self, connection, schema=None, **kw):
        if schema is None:
            query = "SELECT DISTINCT TABLE_SCHEM||'.'||table_name FROM system.catalog"
            params = []
        else:
            query = "SELECT DISTINCT TABLE_SCHEM||'.'||table_name FROM system.catalog WHERE TABLE_SCHEM = ? "
            params = [schema.upper()]
        return connection.execute(query, params) is not None


    def get_columns(self, connection, table_name, schema=None, **kw):
        if schema is None:
            query = "SELECT COLUMN_NAME,  DATA_TYPE, NULLABLE " \
                    "FROM system.catalog " \
                    "WHERE table_name = ? " \
                    "ORDER BY ORDINAL_POSITION"
            params = [table_name.upper()]
        else:
            query = "SELECT COLUMN_NAME, DATA_TYPE, NULLABLE " \
                    "FROM system.catalog " \
                    "WHERE TABLE_SCHEM = ? " \
                    "AND table_name = ? " \
                    "ORDER BY ORDINAL_POSITION"
            params = [schema.upper(), table_name.upper()]

        # get all of the fields for this table
        c = connection.execute(query, params)
        cols = []
        # first always none
        c.fetchone()
        while True:
            row = c.fetchone()
            if row is None:
                break
            name = row[0]
            col_type = COLUMN_DATA_TYPE[row[1]]
            nullable = row[2] == 1 if True else False

            col_d = {
                'name': name,
                'type': col_type,
                'nullable': nullable,
                'default': "",
                'autoincrement': 'auto',
            }

            cols.append(col_d)
        return cols

    def get_pk_constraint(self, conn, table_name, schema=None, **kw):
        return []

    def get_foreign_keys(self, conn, table_name, schema=None, **kw):
        return []

    def get_indexes(self, conn, table_name, schema=None, **kw):
        return []