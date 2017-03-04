"""
SQLAlchemy backend for phoenix
"""
from sqlalchemy.dialects import registry

registry.register("phoenix", "sqlalchemy_phoenix.pyphoenix", "PhoenixDialect_pyphoenix")
registry.register("phoenix.jaydebeapidb", "sqlalchemy_phoenix.jaydebeapidb", "PhoenixDialect_jaydebeapidb")
registry.register("phoenix.pyphoenix", "sqlalchemy_phoenix.pyphoenix", "PhoenixDialect_pyphoenix")