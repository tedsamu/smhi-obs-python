import requests
import json
from string import Template
from typing import Optional
from typing import Dict
from typing import List
from datetime import datetime

class SmhiObs:
    def __init__(self, station: str, cache: bool = True):
        self.station_id = self.__get_station_id(station)
        self.endpoint_template = (
            'https://opendata-download-metobs.smhi.se/api/version/1.0/'
            'parameter/{}/station/{}/period/{}/data.json'
        )
        self.cache = cache
        self.cached_data = {} # type: Dict

    def fetch_hourly_temperature(self, date: str) -> Optional[float]:
        temperature = 1
        return self.__fetch_latest_months_data(date, temperature)

    def fetch_day_average_temperature(self, date: str) -> Optional[float]:
        average_temperature = 2
        return self.__fetch_latest_months_data(date, average_temperature)

    def fetch_day_max_temperature(self, date: str) -> Optional[float]:
        max_temperature = 20
        return self.__fetch_latest_months_data(date, max_temperature)

    def fetch_day_min_temperature(self, date: str) -> Optional[float]:
        min_temperature = 19
        return self.__fetch_latest_months_data(date, min_temperature)

    def fetch_month_average_temperature(self, date: str) -> Optional[float]:
        temperature = 22
        return self.__fetch_latest_months_data(date, temperature)

    @staticmethod
    def get_available_stations() -> dict:
        endpoint = 'https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/2/station.json'
        response = requests.get(endpoint)
        if response.status_code == 200:
            result = json.loads(response.content)
        else:
            raise RuntimeError(
                "Request failed with status code: ", response.status_code)
        stations = {} # type: Dict
        for r in result['station']:
            if r['active'] == True:
                stations[r['name']] = r['id']
        return stations

    @staticmethod
    def print_available_stations() -> None:
        for s, id in SmhiObs.get_available_stations().items():
            print(f'{s}')

    @staticmethod
    def search_station(name: str) -> List:
        stations = SmhiObs.get_available_stations()
        return [(station, id) for station, id in stations.items() if name.lower() in station.lower()]

    def __get_station_id(self, name: str) -> int:
        result = SmhiObs.search_station(name)
        for s, id in result:
            if s.lower() == name.lower():
                return id
        raise ValueError(
            f'Station "{name}" not found. Maybe it is misspelled. Use "SmhiObs.print_available_stations()" to print all available stations.')

    def __fetch_latest_months_data(self, date: str, parameter: int) -> Optional[float]:
        period = 'latest-months'
        result = self.__fetch(self.station_id, parameter, period)
        temperature = None
        for r in result['value']:
            try:
                if r['ref'] == date:
                    temperature = float(r["value"])
                    break
            except:
                if datetime.fromtimestamp(r['date']/1000).strftime("%Y-%m-%d-%H") == date:
                    temperature = float(r["value"])
                    break
        if temperature is None:
            raise ValueError(f'Could not find entry for given date {date}.')
        return temperature

    def __fetch(self, station_id: int, parameter: int, period: str) -> dict:
        endpoint = self.endpoint_template.format(parameter, station_id, period)
        if self.cache:
            try:
                response = self.cached_data[endpoint]
            except KeyError:
                response = requests.get(endpoint)
        else:
            response = requests.get(endpoint)

        if self.cache:
            self.cached_data[endpoint] = response
        if response.status_code == 200:
            result = json.loads(response.content)
        else:
            raise RuntimeError(
                "Request failed with status code: ", response.status_code)
        return result
