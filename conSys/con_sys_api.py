from pydantic import BaseModel, HttpUrl

from conSys.endpoints.endpoints import Endpoint
from conSys.request_bodies import RequestBody


class ConnectedSystemAPIRequest(BaseModel):
    url: HttpUrl
    request_body: RequestBody


class ConnectedSystemsRequestBuilder(BaseModel):
    api_request: ConnectedSystemAPIRequest
    base_url: HttpUrl
    endpoint: Endpoint

    def with_api_url(self, url: HttpUrl):
        self.api_request.url = url
        return self

    def with_server_url(self, server_url: HttpUrl):
        self.base_url = server_url
        return self

    def build_url_from_base(self):
        """
        Builds the full API endpoint URL from the base URL and the endpoint parameters that have been previously
        provided.
        """
        self.api_request.url = f'{self.base_url}/{self.endpoint.create_endpoint()}'
        return self

    def with_api_root(self, api_root: str):
        """
        Optional: Set the API root for the request. This is useful if you want to use a different API root than the
        default one (api).
        :param api_root:
        :return:
        """
        self.endpoint.api_root = api_root
        return self

    def for_resource_type(self, resource_type: str):
        self.endpoint.base_resource = resource_type
        return self

    def with_resource_id(self, resource_id: str):
        self.endpoint.resource_id = resource_id
        return self

    def for_sub_resource_type(self, sub_resource_type: str):
        self.endpoint.sub_component = sub_resource_type
        return self

    def with_secondary_resource_id(self, resource_id: str):
        self.endpoint.secondary_resource_id = resource_id
        return self

    def with_request_body(self, request_body: RequestBody):
        self.api_request.request_body = request_body
        return self

    def build(self):
        # convert endpoint to HttpUrl
        return self.api_request

    def reset(self):
        self.api_request = ConnectedSystemAPIRequest()
        self.endpoint = Endpoint()
        return self
