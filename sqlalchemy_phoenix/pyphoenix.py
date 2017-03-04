from base import PhoenixDialect
import urlparse
import urllib

class PhoenixDialect_pyphoenix(PhoenixDialect):

    driver = "pyphoenix"

    @classmethod
    def dbapi(cls):
        import pyphoenix

        return pyphoenix

    def create_connect_args(self, url):
        phoenix_url = urlparse.urlunsplit(urlparse.SplitResult(
            scheme='http',
            netloc='{}:{}'.format(url.host, url.port or 8765),
            path='/',
            query=urllib.urlencode(url.query),
            fragment='',
        ))
        return [phoenix_url], {'autocommit': True}
