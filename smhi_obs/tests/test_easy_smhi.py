import pytest
from smhi_obs.smhi_obs import SmhiObs
from . import fake_smhi_response_data as fake_data

def fake_response(mocker, content, status_code = fake_data.status_code_ok):
    # Mock GET response from requests package
    response = mocker.Mock()
    response.status_code = status_code
    response.content = content
    return response

def test_get_available_stations(mocker):
    # Patch GET response from requests package
    mocker.patch("smhi_obs.smhi_obs.requests.get",
                 return_value=fake_response(mocker, fake_data.fake_stations_response))

    # Get dict of available stations
    stations = SmhiObs.get_available_stations()
    # Compare stations with true values
    assert(stations == fake_data.fake_stations_correct_values)

def test_print_available_stations(mocker, capsys):
    # Patch GET response from requests package
    mocker.patch("smhi_obs.smhi_obs.requests.get",
                 return_value=fake_response(mocker, fake_data.fake_stations_response))

    # Print and capture available stations
    SmhiObs.print_available_stations()
    captured = capsys.readouterr()
    # Compare stations with true values
    assert captured.out == fake_data.print_stations_correct_values

def test_search_station(mocker):
    # Patch GET response from requests package
    mocker.patch("smhi_obs.smhi_obs.requests.get",
                 return_value=fake_response(mocker, fake_data.fake_stations_response))

    # Get dict of available stations
    stations = SmhiObs.search_station('Abisko')
    # Compare stations with true values
    assert(stations == fake_data.search_stations_correct_values)

def test_fetch_day_temperatures(mocker):
    # Patch GET response from requests package for station check of SmhiObs construction
    mocker.patch("smhi_obs.smhi_obs.requests.get",
                 return_value=fake_response(mocker, fake_data.fake_stations_response))
    obs = SmhiObs('Abisko Aut')

    # Patch GET response from requests package for temperature fetching
    mocker.patch("smhi_obs.smhi_obs.requests.get",
                 return_value=fake_response(mocker, fake_data.fake_min_temperature_response))
    assert obs.fetch_day_min_temperature('2022-10-27') == fake_data.fake_min_temperature_correct_value

    # Patch GET response from requests package for temperature fetching
    mocker.patch("smhi_obs.smhi_obs.requests.get",
                 return_value=fake_response(mocker, fake_data.fake_average_temperature_response))
    assert obs.fetch_day_average_temperature('2022-10-27') == fake_data.fake_average_temperature_correct_value

    # Patch GET response from requests package for temperature fetching
    mocker.patch("smhi_obs.smhi_obs.requests.get",
                 return_value=fake_response(mocker, fake_data.fake_max_temperature_response))
    assert obs.fetch_day_max_temperature('2022-10-27') == fake_data.fake_max_temperature_correct_value

def test_fetch_month_temperatures(mocker):
    # Patch GET response from requests package for station check of SmhiObs construction
    mocker.patch("smhi_obs.smhi_obs.requests.get",
                 return_value=fake_response(mocker, fake_data.fake_stations_response))
    obs = SmhiObs('Abisko Aut')

    # Patch GET response from requests package for temperature fetching
    get_mock = mocker.patch("smhi_obs.smhi_obs.requests.get",
                 return_value=fake_response(mocker, fake_data.fake_month_temperature_response))

    # Check monthly temperatures against true values
    assert obs.fetch_month_average_temperature('2022-09') == fake_data.fake_month_temperature_correct_value[0]
    assert obs.fetch_month_average_temperature('2022-08') == fake_data.fake_month_temperature_correct_value[1]
    assert obs.fetch_month_average_temperature('2022-07') == fake_data.fake_month_temperature_correct_value[2]
    assert obs.fetch_month_average_temperature('2022-06') == fake_data.fake_month_temperature_correct_value[3]

    # Check that cached data was used, i.e. GET request was only called once
    assert get_mock.call_count == 1

def test_fetch_hourly_temperature(mocker):
    # Patch GET response from requests package for station check of SmhiObs construction
    mocker.patch("smhi_obs.smhi_obs.requests.get",
                 return_value=fake_response(mocker, fake_data.fake_stations_response))
    obs = SmhiObs('Abisko Aut')

    # Patch GET response from requests package for temperature fetching
    mocker.patch("smhi_obs.smhi_obs.requests.get",
                 return_value=fake_response(mocker, fake_data.fake_hourly_temperatures_response))
    for h in range(24):
        assert obs.fetch_hourly_temperature(f'2022-10-27-{h:02}') == fake_data.fake_hourly_temperatures_correct_value[h]

def test_no_cache(mocker):
    # Patch GET response from requests package for station check of SmhiObs construction
    mocker.patch("smhi_obs.smhi_obs.requests.get",
                 return_value=fake_response(mocker, fake_data.fake_stations_response))
    # Turn of caching of SMHI api calls
    obs = SmhiObs('Abisko Aut', cache=False)

    # Patch GET response from requests package for temperature fetching
    get_mock = mocker.patch("smhi_obs.smhi_obs.requests.get",
                 return_value=fake_response(mocker, fake_data.fake_month_temperature_response))

    # Check monthly temperatures against true values
    assert obs.fetch_month_average_temperature('2022-09') == fake_data.fake_month_temperature_correct_value[0]
    assert obs.fetch_month_average_temperature('2022-08') == fake_data.fake_month_temperature_correct_value[1]
    assert obs.fetch_month_average_temperature('2022-07') == fake_data.fake_month_temperature_correct_value[2]
    assert obs.fetch_month_average_temperature('2022-06') == fake_data.fake_month_temperature_correct_value[3]

    # Check that cached data was not used, i.e. GET request was called 4 times
    assert get_mock.call_count == 4

def test_misspelled_station(mocker):
    # Patch GET response from requests package for station check of SmhiObs construction
    mocker.patch("smhi_obs.smhi_obs.requests.get",
                 return_value=fake_response(mocker, fake_data.fake_stations_response))
    # Check that constructor raises ValueError if station name does not exist
    with pytest.raises(ValueError):
        obs = SmhiObs('Abisok')

def test_failed_GET_response_for_stations(mocker):
    # Patch GET response from requests package
    response = mocker.Mock()
    response.status_code = fake_data.status_code_fail
    mocker.patch("smhi_obs.smhi_obs.requests.get", return_value=response)

    # Check that call raises RuntimeError if SMHI api call fails
    with pytest.raises(RuntimeError):
        stations = SmhiObs.get_available_stations()

def test_failed_GET_response_for_data(mocker):
    # Patch GET response from requests package for station check of SmhiObs construction
    mocker.patch("smhi_obs.smhi_obs.requests.get",
                 return_value=fake_response(mocker, fake_data.fake_stations_response))
    obs = SmhiObs('Abisko Aut')

    # Patch GET response from requests package for temperature fetching
    mocker.patch("smhi_obs.smhi_obs.requests.get",
                 return_value=fake_response(mocker,
                                            fake_data.fake_month_temperature_response,
                                            fake_data.status_code_fail))

    # Check that call raises RuntimeError if SMHI api call fails
    with pytest.raises(RuntimeError):
        obs.fetch_month_average_temperature('2022-09')
