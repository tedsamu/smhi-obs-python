# smhi_obs_python ![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/tedsamu/smhi-obs-python/python-app.yml) ![GitHub](https://img.shields.io/github/license/tedsamu/smhi-obs-python)
**An easy python interface for the SMHI open data API.**

## Description
The goal of this project is to supply you with an easy python interface for the 
SMHI (Swedish Meteorological and Hydrological Institute) 
[Meteorological Observations](https://opendata.smhi.se/apidocs/metobs/index.html) open data.

**Simplicity** and **ease of use** has been guiding stars when developing this project. This means that 
more advanced features may be missing, however the implemented functionality is robust and esay to use.

**Currently only temperature observations are available.**

## Usage
The following minimal example will fetch the average temperature of 2022-11-01 for Stockholm Arlanda Airport-python-python.
```
# Get yesterdays date in YYYY-mm-dd format.
date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

# Setup observation object for specific station
obs = SmhiObs('Stockholm-Arlanda Flygplats')

# Fetch average temperature of given date
avg_temperature = obs.fetch_day_average_temperature(date)
```
For more examples see the [examples](smhi_obs/examples/) directory. Available stations can be found using the [print_available_stations.py](smhi_obs/examples/print_available_stations.py) example.

## Functionality
### Meteorological Observations
The currently available data is:
* **Minimum, maximum and average temperature of a given date**
  * See [examples/get_yesterdays_temperature.py](smhi_obs/examples/get_yesterdays_temperature.py) for reference.
* **Average temperature of a given month**
* **Hourly temperature of a given date and time**
  * See [examples/get_yesterdays_hourly_temperatures.py](smhi_obs/examples/get_yesterdays_hourly_temperatures.py)

In addition, there are some helper functions to search and list available stations 
(see [examples/print_available_stations.py](smhi_obs/examples/print_available_stations.py)).

*Note: All above functionality is tested in [tests/test_easy_smhi.py](smhi_obs/tests/test_easy_smhi.py) and same file can be used as reference.*

*Note: The date must not be today or in the future. 
    Nor can it be more than 4 months back, due to constraints in the SMHI API. The latter could be solved and I 
    encourage you to contribute with a nice implementation.*

### Cached data
To minimize slow calls to the SMHI REST API responses will be cached by default. This means that, if the data you are 
trying to fetch has already been downloaded during another call, the data will be retrieved from memory. This 
drastically increases speed when possible. This is done "under the hood" and nothing the user needs to think about. If 
this is an undesired behavior it can be disabled:
```
SmhiObs('Stockholm-Arlanda Flygplats', cache=False) # Disable cache
```

## Installation
For testing or development purposes you can use the [Dockerfile](dev/Dockerfile) available in the [dev](dev) directory. This includes all 
dependencies needed for running and testing. It also includes Pycharm Community edition. For usage see [dev/README.md](dev/README.md).

### Minimum requirements
If you want to go further than playing around in the above docker container, you will at least need the 
[Requests](https://pypi.org/project/requests/) package. 

For additional non-essential dependencies (e.g. for testing) see [dev/Dockerfile](dev/Dockerfile).

## Support
Easiest is to use the dedicated issue tracker.

## Contributing
Contributions are welcome. Reach out or put up a MR. 

## License
[MIT](LICENSE)
