from consys4py import Systems, SamplingFeatures, Datastreams, Procedures, ControlChannels, Observations, \
    Commands

server_url = 'http://localhost:8282/sensorhub'


def test_delete_all_command_status_reports():
    commands = Commands.list_all_commands(server_url).json()
    for command in commands["items"]:
        reports = Commands.list_command_status_reports(server_url, command["id"]).json()
        for report in reports["items"]:
            Commands.delete_command_status_report_by_id(server_url, report["id"])
            print(f"Deleted command status report {report['id']}")


def test_delete_all_commands():
    commands = Commands.list_all_commands(server_url).json()
    for command in commands["items"]:
        Commands.delete_command_by_id(server_url, command["id"])
        print(f"Deleted command {command['id']}")


def test_delete_all_observations():
    obs_list = Observations.list_all_observations(server_url).json()
    print(obs_list)
    for obs in obs_list["items"]:
        print(obs)
        Observations.delete_observation_by_id(server_url, obs["id"])
        print(f"Deleted observation {obs['id']}")


def test_delete_all_collections():
    pass


def test_delete_all_sampling_features():
    sf_list = SamplingFeatures.list_all_sampling_features(server_url).json()
    print(sf_list)

    for sf in sf_list["items"]:
        print(sf)

        SamplingFeatures.delete_sampling_feature_by_id(server_url, sf["id"])
        print(f"Deleted sampling feature {sf['id']}")


def test_delete_all_control_streams():
    control_streams = ControlChannels.list_all_control_streams(server_url).json()
    print(control_streams)

    for cs in control_streams["items"]:
        print(cs)

        ControlChannels.delete_control_stream_by_id(server_url, cs["id"])
        print(f"Deleted control stream {cs['id']}")


def test_delete_all_datastreams():
    ds_list = Datastreams.list_all_datastreams(server_url).json()
    print(ds_list)

    for ds in ds_list["items"]:
        print(ds)

        Datastreams.delete_datastream_by_id(server_url, ds["id"])
        print(f"Deleted datastream {ds['id']}")


def test_delete_all_procedures():
    proc_list = Procedures.list_all_procedures(server_url).json()
    print(proc_list)

    for proc in proc_list["items"]:
        print(proc)

        Procedures.delete_procedure_by_id(server_url, proc["id"])
        print(f"Deleted procedure {proc['id']}")


def test_delete_all_systems():
    sys_list = Systems.list_all_systems(server_url).json()["items"]
    print(sys_list)

    for system in sys_list:
        print(system)

        Systems.delete_system_by_id(server_url, system["id"])
        print(f"Deleted system {system['id']}")
