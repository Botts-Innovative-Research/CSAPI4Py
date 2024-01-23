import requests
from pydantic import HttpUrl

from conSys.con_sys_api import ConnectedSystemsRequestBuilder
from conSys.constants import APITerms


def list_all_commands(server_addr: HttpUrl, api_root: str = APITerms.API.value):
    """
    Lists all commands
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.COMMANDS.value)
                   .build_url_from_base()
                   .build())
    resp = requests.get(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def list_commands_of_control_channel(server_addr: HttpUrl, control_channel_id: str, api_root: str = APITerms.API.value):
    """
    Lists all commands of a control channel
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.CONTROL_STREAMS.value)
                   .with_resource_id(control_channel_id)
                   .for_resource_type(APITerms.COMMANDS.value)
                   .build_url_from_base()
                   .build())
    resp = requests.get(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def send_commands_to_specific_control_stream(server_addr: HttpUrl, control_stream_id: str, request_body: dict,
                                             api_root: str = APITerms.API.value):
    """
    Sends a command to a control stream by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.CONTROL_STREAMS.value)
                   .with_resource_id(control_stream_id)
                   .for_resource_type(APITerms.COMMANDS.value)
                   .with_request_body(request_body)
                   .build_url_from_base()
                   .build())
    resp = requests.post(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def retrieve_command_by_id(server_addr: HttpUrl, command_id: str, api_root: str = APITerms.API.value):
    """
    Retrieves a command by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.COMMANDS.value)
                   .with_resource_id(command_id)
                   .build_url_from_base()
                   .build())
    resp = requests.get(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def update_command_description(server_addr: HttpUrl, command_id: str, request_body: dict,
                               api_root: str = APITerms.API.value):
    """
    Updates a command's description by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.COMMANDS.value)
                   .with_resource_id(command_id)
                   .with_request_body(request_body)
                   .build_url_from_base()
                   .build())
    resp = requests.put(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def delete_command_by_id(server_addr: HttpUrl, command_id: str, api_root: str = APITerms.API.value):
    """
    Deletes a command by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.COMMANDS.value)
                   .with_resource_id(command_id)
                   .build_url_from_base()
                   .build())
    resp = requests.delete(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def list_command_status_reports(server_addr: HttpUrl, command_id: str, api_root: str = APITerms.API.value):
    """
    Lists all status reports of a command by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.COMMANDS.value)
                   .with_resource_id(command_id)
                   .for_resource_type(APITerms.STATUS.value)
                   .build_url_from_base()
                   .build())
    resp = requests.get(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def add_command_status_reports(server_addr: HttpUrl, command_id: str, request_body: dict,
                               api_root: str = APITerms.API.value):
    """
    Adds a status report to a command by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.COMMANDS.value)
                   .with_resource_id(command_id)
                   .for_resource_type(APITerms.STATUS.value)
                   .with_request_body(request_body)
                   .build_url_from_base()
                   .build())
    resp = requests.post(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def retrieve_command_status_report_by_id(server_addr: HttpUrl, command_id: str, status_report_id: str,
                                         api_root: str = APITerms.API.value):
    """
    Retrieves a status report of a command by its id and status report id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.COMMANDS.value)
                   .with_resource_id(command_id)
                   .for_resource_type(APITerms.STATUS.value)
                   .with_secondary_resource_id(status_report_id)
                   .build_url_from_base()
                   .build())
    resp = requests.get(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def update_command_status_report_by_id(server_addr: HttpUrl, command_id: str, status_report_id: str,
                                       request_body: dict, api_root: str = APITerms.API.value):
    """
    Updates a status report of a command by its id and status report id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.COMMANDS.value)
                   .with_resource_id(command_id)
                   .for_resource_type(APITerms.STATUS.value)
                   .with_secondary_resource_id(status_report_id)
                   .with_request_body(request_body)
                   .build_url_from_base()
                   .build())
    resp = requests.put(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def delete_command_status_report_by_id(server_addr: HttpUrl, command_id: str, status_report_id: str,
                                       api_root: str = APITerms.API.value):
    """
    Deletes a status report of a command by its id and status report id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.COMMANDS.value)
                   .with_resource_id(command_id)
                   .for_resource_type(APITerms.STATUS.value)
                   .with_secondary_resource_id(status_report_id)
                   .build_url_from_base()
                   .build())
    resp = requests.delete(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()
