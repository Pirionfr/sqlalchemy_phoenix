from base import PhoenixDialect
import urlparse
import urllib

class PhoenixDialect_phoenixdb(PhoenixDialect):

    driver = "phoenixdb"

    @classmethod
    def dbapi(cls):
        import phoenixdb

        return phoenixdb

    def create_connect_args(self, url):
        phoenix_url = urlparse.urlunsplit(urlparse.SplitResult(
            scheme='http',
            netloc='{}:{}'.format(url.host, url.port or 8765),
            path='/',
            query=urllib.urlencode(url.query),
            fragment='',
        ))
        return [phoenix_url], {'autocommit': True}
