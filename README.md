# smhi_obs_python
**An easy python interface for the SMHI open data API.**

## Description
The goal of this project is to supply you with an easy python interface for the 
SMHI (Swedish Meteorological and Hydrological Institute) 
[Meteorological Observations](https://opendata.smhi.se/apidocs/metobs/index.html) open data.

The observations data collection includes historical data for weather related measures, e.g. temperatures, 
wind speeds and precipitation. See more details in the [Functionality](#functionality) section.

**Simplicity** and **ease of use** has been guiding stars when developing this project. This means that 
more advanced features may be missing, however the implemented functionality is robust and esay to use.

The project is currently under early development and might be subject to API changes until its first stable 
release(1.0).

## Usage
The following minimal example will fetch the average temperature of 2022-11-01 for Stockholm Arlanda Airport 
using the meteorological observation module.
```
obs = SmhiObs('Stockholm-Arlanda Flygplats')
avg_temperature = obs.fetch_day_average_temperature('2022-11-01')
```
For more examples see the `examples` directory. Available stations can be found using the 
`print_available_stations.py` example.

## Functionality
### Meteorological Observations
The currently available data is:
* **Minimum, maximum and average temperature of a given date**
  * See `examples/get_yesterdays_weather.py` for reference.
* **Average temperature of a given month**

In addition, there are some helper functions to search and list available stations 
(see `examples/print_available_stations.py`).

*Note: All above functionality is tested in `tests/test_easy_smhi.py` and same file can be used as reference.*

*Note: The date must not be today or in the future. 
    Nor can it be more than 4 months back, due to constraints in the SMHI API. This could be solved and I 
    encourage you to contribute with a nice implementation.*

### Cached data
To minimize slow calls to the SMHI REST API responses will be cached by default. This means that, if the data you are 
trying to fetch has already been downloaded during another call, the data will be retrieved from memory. This 
drastically increases speed when possible. This is done "under the hood" and nothing the user needs to think about. If 
this is an undesired behavior it can be disabled.
```
SmhiObs('Stockholm-Arlanda Flygplats', cache=False) # Disable cache
```

## Installation
For testing or development purposes you can use the Dockerfile available in the `dev` directory. This includes all 
dependencies needed for running and testing. It also includes Pycharm Community edition. For usage see `dev/README.md`.

### Minimum requirements
If you want to go further than playing around in the above docker container, you will at least need the 
[Requests](https://pypi.org/project/requests/) package. 

For additional non-essential dependencies (e.g. for testing) see `dev/Dockerfile`.

## Support
Easiest is to use the dedicated issue tracker.

## Roadmap
Planned updates:
* [Hourly temperature observations](https://opendata.smhi.se/apidocs/metfcst/index.html)

## Contributing
Contributions are welcome. Reach out or put up a MR. 

## License
MIT
