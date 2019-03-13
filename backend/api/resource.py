from protorpc import remote, messages, message_types

from backend import api, resource
from backend.oauth2 import oauth2


class Data(messages.Message):
    test = messages.IntegerField(1)


class FetchResponse(messages.Message):
    data = messages.MessageField(Data, 1)
    success = messages.BooleanField(2)


@api.endpoint(path="resource", title="Resource API")
class Resource(remote.Service):

    @oauth2.required()
    @remote.method(message_types.VoidMessage, FetchResponse)
    def fetch(self, request):
        rsrc = resource.Resource.fetch()

        return FetchResponse(
            data=Data(
                test=rsrc["data"]["test"]
            ),
            success=rsrc["success"]
        )
