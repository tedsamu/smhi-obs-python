#!/usr/bin/python3
#
# Example demonstrating how to fetch historical temperature observations.
# More specific, this example will print min, average and max temperatures
# from yesterday as captured by the Arlanda station.
#
# Copyright (c) 2022 Ted Samuelsson

import sys
import os
from datetime import datetime, timedelta

# Add parent directory (smhi_obs) to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

# Import the SMHI observation class from smhi_obs package
from smhi_obs import SmhiObs # type: ignore[attr-defined]

if __name__ == '__main__':
    # Set station name
    station = 'Stockholm-Arlanda Flygplats'
    # Get yesterdays date
    date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

    # Create SmhiObs object
    obs = SmhiObs(station)

    # Print temperature for each hour
    print(f'Date: {date}')
    print(f'Station: {station}\n')
    print('Hour    Temperature')
    print('-----------------------')
    for h in range(24):
        # Fetch temperature value
        temperature = obs.fetch_hourly_temperature(date+f'-{h:02}')
        print(f'{h:2}      {temperature:6.1f}')
    print('-----------------------')
