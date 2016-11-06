#!/usr/bin/env python
"""
Setup for SQLAlchemy backend for phoenixdb
"""
from setuptools import find_packages, setup



setup_params = dict(
    name="sqlalchemy_phoenix",
    version='0.3.0',
    description="SQLAlchemy dialect for Phoenix",
    author="Dimitri Capitaine",
    author_email="grytes29@gmail.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Database :: Front-Ends',
    ],
    keywords='Phoenix SQLAlchemy',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "sqlalchemy.dialects":
            ["phoenix = sqlalchemy_phoenix.phoenix_db:PhoenixDialect_phoenixdb",
             "phoenix.jaydebeapidb = sqlalchemy_phoenix.jaydebeapidb:PhoenixDialect_jaydebeapidb",
             "phoenix.phoenixdb = sqlalchemy_phoenix.phoenix_db:PhoenixDialect_phoenixdb"]
    },
    license="MIT",
    install_requires=['jaydebeapi','phoenixdb','sqlalchemy'],
)

if __name__ == '__main__':
    setup(**setup_params)