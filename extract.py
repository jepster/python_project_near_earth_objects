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

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path) -> list:
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # [DONE] TODO: Load NEO data from the given CSV file.

    near_earth_object_collection = []

    with open(neo_csv_path) as infile:
        reader = csv.reader(infile)
        next(reader)
        for row in reader:
            def is_hazardous(value) -> bool:
                hazardous = False
                if value == 'Y':
                    hazardous = True
                return hazardous

            def get_diameter(value) -> float:
                diameter_default = float('nan')
                try:
                    return float(value)
                except ValueError:
                    return diameter_default

            near_earth_object = NearEarthObject(row[3], row[4], get_diameter(row[15]), is_hazardous(row[7]))
            near_earth_object_collection.append(near_earth_object)

    return near_earth_object_collection


def load_approaches(cad_json_path) -> list:
    """Read close approach data from a JSON file.

    :param str cad_json_path: A path to a JSON file containing data about close approaches.
    :return list: A collection of `CloseApproach`es.
    """
    # [DONE] TODO: Load close approach data from the given JSON file.

    close_approach_collection = []

    with open(cad_json_path) as infile:
        json_content = json.load(infile)

        for item in json_content['data']:
            near_earth_object = NearEarthObject(item[0])
            close_approach = CloseApproach(item[3], _string_to_float(item[4]), _string_to_float(item[7]), near_earth_object)
            close_approach_collection.append(close_approach)

    return close_approach_collection


def _string_to_float(value: str) -> float:
    diameter_default = float('nan')
    try:
        return float(value)
    except ValueError:
        return diameter_default