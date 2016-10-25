"""
SQLAlchemy backend for phoenix
"""
from sqlalchemy.dialects import registry

registry.register("phoenix", "sqlalchemy_phoenix.phoenix_db", "PhoenixDialect_phoenixdb")
registry.register("phoenix.jaydebeapidb", "sqlalchemy_phoenix.jaydebeapidb", "PhoenixDialect_jaydebeapidb")
registry.register("phoenix.phoenixdb", "sqlalchemy_phoenix.phoenix_db", "PhoenixDialect_phoenixdb")