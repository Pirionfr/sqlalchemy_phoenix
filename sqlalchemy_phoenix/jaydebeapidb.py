from base import PhoenixDialect


class PhoenixDialect_jaydebeapidb(PhoenixDialect):
    _phoenix_driver = 'org.apache.phoenix.jdbc.PhoenixDriver'
    driver = "jaydebeapidb"

    @classmethod
    def dbapi(cls):
        import jaydebeapi
        from jaydebeapi import _DEFAULT_CONVERTERS, _java_to_py
        _DEFAULT_CONVERTERS.update({'BIGINT': _java_to_py('longValue')})

        return jaydebeapi

    def create_connect_args(self, url):
        opts = url.translate_connect_args()
        opts.update(url.query)
        driver_url = 'jdbc:phoenix:' + opts['host'] + ':' + str(opts['port']) + ':/' + opts['database']

        return [self._phoenix_driver], {'driver_args': [driver_url, '', ''], 'jars': opts['jars']}
