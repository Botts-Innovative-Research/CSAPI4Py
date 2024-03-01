from abc import ABC
from dataclasses import dataclass

from conSys4Py import APIResourceTypes, APITerms


def determine_parent_type(res_type: APIResourceTypes):
    match res_type:
        case APIResourceTypes.SYSTEM:
            return APIResourceTypes.SYSTEM
        case APIResourceTypes.COLLECTION:
            return None
        case APIResourceTypes.CONTROL_CHANNEL:
            return APIResourceTypes.SYSTEM
        case APIResourceTypes.COMMAND:
            return APIResourceTypes.CONTROL_CHANNEL
        case APIResourceTypes.DATASTREAM:
            return APIResourceTypes.SYSTEM
        case APIResourceTypes.OBSERVATION:
            return APIResourceTypes.DATASTREAM
        case APIResourceTypes.SYSTEM_EVENT:
            return APIResourceTypes.SYSTEM
        case APIResourceTypes.SAMPLING_FEATURE:
            return APIResourceTypes.SYSTEM
        case APIResourceTypes.PROCEDURE:
            return None
        case APIResourceTypes.PROPERTY:
            return None
        case APIResourceTypes.SYSTEM_HISTORY:
            return None
        case APIResourceTypes.DEPLOYMENT:
            return None
        case _:
            return None


def resource_type_to_endpoint(res_type: APIResourceTypes, parent_type: APIResourceTypes = None):
    if parent_type is APIResourceTypes.COLLECTION:
        return APITerms.ITEMS.value

    match res_type:
        case APIResourceTypes.SYSTEM:
            return APITerms.SYSTEMS.value
        case APIResourceTypes.COLLECTION:
            return APITerms.COLLECTIONS.value
        case APIResourceTypes.CONTROL_CHANNEL:
            return APITerms.CONTROL_STREAMS.value
        case APIResourceTypes.COMMAND:
            return APITerms.COMMANDS.value
        case APIResourceTypes.DATASTREAM:
            return APITerms.DATASTREAMS.value
        case APIResourceTypes.OBSERVATION:
            return APITerms.OBSERVATIONS.value
        case APIResourceTypes.SYSTEM:
            return APITerms.SYSTEMS.value
        case APIResourceTypes.SYSTEM_EVENT:
            return APITerms.SYSTEM_EVENTS.value
        case APIResourceTypes.SAMPLING_FEATURE:
            return APITerms.SAMPLING_FEATURES.value
        case APIResourceTypes.PROCEDURE:
            return APITerms.PROCEDURES.value
        case APIResourceTypes.PROPERTY:
            return APITerms.PROPERTIES.value
        case APIResourceTypes.SYSTEM_HISTORY:
            return APITerms.HISTORY.value
        case APIResourceTypes.DEPLOYMENT:
            return APITerms.DEPLOYMENTS.value
        case _:
            raise ValueError('Invalid resource type')


@dataclass
class APIHelper(ABC):
    server_url = None
    api_endpoint = "/api"
    username = None
    password = None
    user_auth = False

    def create_resource(self, res_type: APIResourceTypes, json_data: any, parent_res_id: str = None):
        """
        Creates a resource of the given type with the given data, will attempt to create a sub-resource if parent_res_id
        is provided.
        :param res_type:
        :param json_data:
        :param parent_res_id:
        :return:
        """
        pass

    def retrieve_resource(self, res_type: APIResourceTypes, res_id: str, parent_res_id: str = None,
                          from_collection: bool = False,
                          collection_id: str = None):
        pass

    def update_resource(self, res_type: APIResourceTypes, res_id: str, json_data: any, parent_res_id: str = None):
        pass

    def delete_resource(self, res_type: APIResourceTypes, res_id: str, parent_res_id: str = None):
        pass

    # Helpers
    def resource_url_resolver(self, res_type: APIResourceTypes, res_id: str, parent_res_id: str = None,
                              from_collection: bool = False):
        if res_type is None:
            raise ValueError('Resource type must contain a valid APIResourceType')
        if res_type is APIResourceTypes.COLLECTION and from_collection:
            raise ValueError('Collections are not sub-resources of other collections')

        parent_type = None
        if parent_res_id and not from_collection:
            parent_type = determine_parent_type(res_type)
        elif parent_res_id and from_collection:
            parent_type = APIResourceTypes.COLLECTION

        return self.construct_url(parent_type, res_id, res_type, parent_res_id)

    def construct_url(self, parent_type, res_id, res_type, parent_res_id):
        # TODO: Test for less common cases to ensure that the URL is being constructed correctly
        base_url = f'{self.server_url}/{self.api_endpoint}'
        resource_endpoint = resource_type_to_endpoint(res_type, parent_type)
        url = f'{base_url}/{resource_endpoint}'

        if parent_type:
            parent_endpoint = resource_type_to_endpoint(parent_type)
            url = f'{base_url}/{parent_endpoint}/{parent_res_id}/{resource_endpoint}'

        if res_id:
            url = f'{url}/{res_id}'

        return url
