Tutorials
====================

.. warning::

    This is a work in progress, some features may change and packages may move or be removed
    before the 1.0 release.

Using the API
============================
There are three main ways to interact with the API

1. Direct API calls
-----------------------------------------
In the modules for parts 1 and 2, there are separate files that represent the different parts of the API. These files
contain methods for interacting with the remote server directly.

2. Default API Helper
-----------------------------------------
Using the Default API helper allows for repeated calls to the same API server. This is useful when
building a library on top of  this project.

3. Custom API Requests
-----------------------------------------
If you need the most flexibility, you can create custom requests using the request builder and API helper objects

.. note::

    The following examples will not convert the responses back into Objects, but it is possible to do so
    using the appropriate class's `model_validate` method on the response object's string representation.

Interacting with Systems
============================

List Systems
-----------------------------------------
.. note::

    Using a direct call from `Systems` file
.. code-block:: python

    from consys4py import Systems

    Systems.list_all_systems(server_url)

Retrieve Specific System
-----------------------------------------

.. code-block:: python

    from consys4py import Systems

    Systems.retrieve_system_by_id(server_url, system_id)

Add/Create System
-----------------------------------------
The method for creating a new system does take a string or properly structured `dict`.
For ease of use, the `SmlJSONBody` or `GeoJSONBody` can be used. They use Pydantic to validate the data.
Just be sure to convert them to a JSON string before passing them to the `create_new_systems` method.

.. code-block:: python

    from consys4py import Systems

    sml = SmlJSONBody(object_type='SimpleProcess', id=str(random.randint(1000, 9999)),
                           description="A Test System inserted from the Python Connected Systems API Client",
                           unique_id=f'urn:test:client:sml-single', label=f'Test System - SML Single',
                           definition="http://test.com")

    sml_as_str = sml.model_dump_json(exclude_none=True, by_alias=True)
    Systems.create_new_systems(server_url, sml_as_str, uname="test", pword="test",
                               headers=sml_json_headers)

Datastreams and Observations
============================

Add a Datastream and Observation
------------------------------------------------------------
.. note::

    This assumes that the user knows the system id and the datastream id

.. code-block:: python

    from consys4py import Datastreams

    time_schema = TimeSchema(label="Test Datastream Time", definition="http://test.com/Time", name="timestamp",
                             uom=URI(href="http://test.com/TimeUOM"))
    bool_schema = BooleanSchema(label="Test Datastream Boolean", definition="http://test.com/Boolean",
                                name="testboolean")
    datarecord_schema = SWEDatastreamSchema(encoding=JSONEncoding(), obs_format=ObservationFormat.SWE_JSON.value,
                                            record_schema=DataRecordSchema(label="Test Datastream Record",
                                                                           definition="http://test.com/Record",
                                                                           fields=[time_schema, bool_schema]))

    datastream_body = DatastreamBodyJSON(name="Test Datastream", output_name="Test Output #1", datastream_schema=datarecord_schema)
    temp_test_json = datastream_body.model_dump_json(exclude_none=True, by_alias=True)

    resp = Datastreams.add_datastreams_to_system(server_url, retrieved_systems[1]['id'],
                                                 datastream_body.model_dump_json(exclude_none=True, by_alias=True),
                                                 headers=json_headers)

    the_time = datetime.utcnow().isoformat() + 'Z'
    time_millis = test_time_start.timestamp() * 1000

    obs = ObservationOMJSONInline(phenomenon_time=the_time,
                                  result_time=the_time,
                                  result={
                                      "timestamp": time_millis,
                                      "testboolean": True
                                  })
    print(f'Observation: {obs.model_dump_json(exclude_none=True, by_alias=True)}')
    resp = Observations.add_observations_to_datastream(server_url, ds_id,
                                                       obs.model_dump_json(exclude_none=True, by_alias=True),
                                                       headers=json_headers)
