from src.consys4py.con_sys_api import ConnectedSystemsRequestBuilder


def test_get_params():
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url('http://localhost:8282/sensorhub')
                   .with_api_root('api')
                   .for_resource_type('systems')
                   .with_params({'id': [YOUR_UID_HERE]})
                   .build_url_from_base()
                   .with_request_method('GET')
                   .build())
    api_request.params = {'id': [YOUR_UID_HERE]}
    api_request.make_request()
