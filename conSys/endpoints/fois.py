import requests
import conSys.endpoints.system_ep as system

from conSys.constants import APITerms


def get_foi(node_api_endpoint=None, params=None, foi_id=None):
    """
    Returns a list of FOIs or a single FOI if foi_id is provided.
    :param node_api_endpoint:
    :param params:
    :param foi_id:
    :return:
    """
    base_url = f'{node_api_endpoint}/{APITerms.FOIS.value}'

    if foi_id is not None:
        base_url += f'/{foi_id}'

    r = requests.get(base_url, params=params)

    if r.status_code == 200:
        return r.json()
    elif not r.ok:
        raise ValueError(f'Error getting FOI: {r.status_code}')


def get_system_fois(node_api_endpoint=None, params=None, system_id=None):
    return system.get_system_fois(node_api_endpoint=node_api_endpoint, params=params, system_id=system_id)


def get_foi_history(node_api_endpoint=None, params=None, foi_id=None, version=None):
    """
    Returns a list of FOI history or a specific version of a feature description
    :param node_api_endpoint:
    :param params:
    :param foi_id:
    :param version:
    :return:
    """
    base_url = f'{node_api_endpoint}/{APITerms.FOIS.value}/{foi_id}/history'

    if version is not None:
        base_url += f'/{version}'

    r = requests.get(base_url, params=params)

    if r.status_code == 200:
        return r.json()
    elif not r.ok:
        raise ValueError(f'Error getting FOI history: {r.status_code}')


def get_foi_members(node_api_endpoint=None, params=None, foi_id=None):
    """
    List or search members of a feature collection. By default, only direct members are listed unless the "parent"
    query parameter is set to "*". Likewise, only the current version of each feature is listed unless the
    "validTime" query parameter is set. Individual members can be retrieved by ID directly on the root "features"
    collection.
    :param node_api_endpoint: 
    :param params:
    :param foi_id:
    :return:
    """
    base_url = f'{node_api_endpoint}/{APITerms.FOIS.value}/{foi_id}/members'

    r = requests.get(base_url, params=params)

    if r.status_code == 200:
        return r.json()
    elif not r.ok:
        raise ValueError(f'Error getting FOI members: {r.status_code}')


def post_foi(node_api_endpoint=None, foi=None):
    """
    Posts a top level FOI to the node. For postin
    :param node_api_endpoint:
    :param foi:
    :return:
    """
    base_url = f'{node_api_endpoint}/{APITerms.FOIS.value}'

    r = requests.post(base_url, json=foi)

    if r.status_code == 201:
        return r.json()
    elif not r.ok:
        raise ValueError(f'Error posting FOI: {r.status_code}')


def post_foi_history(node_api_endpoint=None, foi_id=None, history=None):
    """
    Add a feature description valid for a certain time period to the history. The feature description must have a
    validTime property and its value cannot intersect the validity time period of any other description already in
    the history (except for time periods ending at 'now').
    :param node_api_endpoint:
    :param foi_id:
    :param history:
    :return:
    """
    base_url = f'{node_api_endpoint}/{APITerms.FOIS.value}/{foi_id}/history'

    r = requests.post(base_url, json=history)

    if r.status_code == 201:
        return r.json()
    elif not r.ok:
        raise ValueError(f'Error posting FOI history: {r.status_code}')


def post_foi_members(node_api_endpoint=None, foi_id=None, member=None):
    """
    Add a new member to a feature collection
    :param node_api_endpoint:
    :param foi_id:
    :param member:
    :return:
    """
    base_url = f'{node_api_endpoint}/{APITerms.FOIS.value}/{foi_id}/members'

    r = requests.post(base_url, json=member)

    if r.status_code == 201:
        return r.json()
    elif not r.ok:
        raise ValueError(f'Error posting FOI members: {r.status_code}')


def put_foi(node_api_endpoint=None, foi_id=None, foi=None):
    """
    Update a specific feature or feature collection resource. This will only update the description of the feature
    that is valid at the current time and its validTime property cannot be changed. For more advanced modifications
    of the feature history, use the "history" sub collection.
    :param node_api_endpoint:
    :param foi_id:
    :param foi:
    :return:
    """
    base_url = f'{node_api_endpoint}/{APITerms.FOIS.value}/{foi_id}'

    r = requests.put(base_url, json=foi)

    if r.status_code == 200:
        return r.json()
    elif not r.ok:
        raise ValueError(f'Error putting FOI: {r.status_code}')


def put_foi_history_version(node_api_endpoint=None, foi_id=None, version=None,
                            history=None):
    """
    Update a specific version of a feature description in the history.
    :param node_api_endpoint:
    :param foi_id:
    :param version:
    :param history:
    :return:
    """
    base_url = f'{node_api_endpoint}/{APITerms.FOIS.value}/{foi_id}/history/{version}'

    r = requests.put(base_url, json=history)

    if r.status_code == 200:
        return r.json()
    elif not r.ok:
        raise ValueError(f'Error putting FOI history: {r.status_code}')
