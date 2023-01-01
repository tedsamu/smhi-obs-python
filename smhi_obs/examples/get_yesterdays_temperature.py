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
from smhi_obs import SmhiObs

if __name__ == '__main__':
    # Set station name
    station = 'Stockholm-Arlanda Flygplats'
    # Get yesterdays date
    date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

    # Create SmhiObs object
    obs = SmhiObs(station)
    # Fetch min, average and max temperature values
    min_temperature = obs.fetch_day_min_temperature(date)
    avg_temperature = obs.fetch_day_average_temperature(date)
    max_temperature = obs.fetch_day_max_temperature(date)

    # Print min, average and max temperature values
    print('Date       Station                           Min    Avg    Max')
    print('--------------------------------------------------------------')
    print(f'{date} {station:30s} {min_temperature:6.1f} {avg_temperature:6.1f} {max_temperature:6.1f}')
    print('--------------------------------------------------------------')
