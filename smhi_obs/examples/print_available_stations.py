#!/usr/bin/python3
#
# Example demonstrating the usage of the print_available_stations() method.
# The method is static and thus available without creating an SmhiObs object
# first. Running the example will print all available stations to the terminal.
#
# Copyright (c) 2022 Ted Samuelsson

import sys
import os

# Add paraent directory (smhi_obs) to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

# Import the SMHI observation class from smhi_obs package
from smhi_obs import SmhiObs

if __name__ == '__main__':
    # Print all available stations
    SmhiObs.print_available_stations()
