"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from near_earth_object import NearEarthObject
from close_approach import CloseApproach


def load_neos(neo_csv_path) -> list:
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about
    near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    csv_list = []

    with open(neo_csv_path, 'r') as csv_to_read:
        data_from_csv = csv.DictReader(csv_to_read)
        for each_row_csv in data_from_csv:
            csv_list.append(NearEarthObject(**each_row_csv))
    return csv_list


def load_approaches(cad_json_path) -> list:
    """Read close approach data from a JSON file.

    :param str cad_json_path: A path to a JSON file containing data about close approaches.
    :return list: A collection of `CloseApproach`es.
    """

    json_list = []

    with open(cad_json_path) as json_to_read:
        data_from_json = json.load(json_to_read)
        for each_row_json in data_from_json['data']:
            each_row_json = dict(zip(data_from_json['fields'], each_row_json))
            json_list.append(CloseApproach(**each_row_json))
    return json_list


def _string_to_float(value: str) -> float:
    diameter_default = float('nan')
    try:
        return float(value)
    except ValueError:
        return diameter_default
