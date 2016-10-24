"""
SQLAlchemy backend for phoenix
"""
from sqlalchemy.dialects import registry


registry.register("phoenix.jaydebeapidb", "sqlalchemy_phoenix.jaydebeapidb", "PhoenixDialect_jaydebeapidb")
