import unittest

from near_earth_object import NearEarthObject
from close_approach import CloseApproach


class TestModels(unittest.TestCase):

    def test_object_initialized_by_NearEarthObject_model(self):
        near_earth_object = NearEarthObject('designation_value', 'iau_name_value', 'diameter_value', True)
        self.assertEqual("NearEarthObject({'designation': 'designation_value', 'iau_name': 'iau_name_value', "
                         "'diameter': 'diameter_value', 'hazardous': True, "
                         "'close_approach_collection': None})", near_earth_object.__str__())

    def test_edge_cases_by_initialization_of_NearEarthObject_model(self):
        near_earth_object = NearEarthObject('designation_value')
        self.assertEqual("NearEarthObject({'designation': 'designation_value', 'iau_name': None, 'diameter': nan, "
                         "'hazardous': None, 'close_approach_collection': None})", near_earth_object.__str__())

    def test_close_approach_object_init(self):
        near_earth_obj = NearEarthObject('designation_value')
        close_approach_obj = CloseApproach('2020-Dec-31 12:00', 3.1, 55.55, near_earth_obj)
        self.assertEqual('Approach time of designation_value was at 2020-12-31 12:00', close_approach_obj.time_str)
        self.assertEqual("A CloseApproach time=Approach time of designation_value was at 2020-12-31 12:00 distance=3.1 "
                         "velocity=55.55 neo=NearEarthObject({'designation': 'designation_value', 'iau_name': None, "
                         "'diameter': nan, 'hazardous': None, 'close_approach_collection': None})",
                         close_approach_obj.__str__())