import json

from google.appengine.api import urlfetch

from backend import error


class ResourceUnavailable(error.Error):
    pass


class Resource(object):

    @classmethod
    def fetch(cls):
        url = 'https://www.mocky.io/v2/5c76b900320000b31cf46398'
        try:
            result = urlfetch.fetch(url, validate_certificate=True)
            if result.status_code == 200:
                return json.loads(result.content)
            else:
                raise ResourceUnavailable(str(result.status_code))
        except urlfetch.Error as e:
            raise ResourceUnavailable('Caught exception fetching url: %s' % e)
