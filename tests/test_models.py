import unittest

from models import NearEarthObject, CloseApproach


class TestModels(unittest.TestCase):

    def test_object_initialized_by_NearEarthObject_model(self):
        info = {
            'designation': 'designation_value',
            'name': 'name_value',
            'diameter': 3.11
        }
        near_earth_object = NearEarthObject(info)
        self.assertEqual("NearEarthObject({'designation': 'designation_value', 'name': 'name_value', "
                         "'diameter': 3.11, 'hazardous': False})", near_earth_object.__str__())

    def test_edge_cases_by_initialization_of_NearEarthObject_model(self):
        info = {
            'designation': 'designation_value',
        }
        near_earth_object = NearEarthObject(info)
        print("NearEarthObject({'designation': 'designation_value', 'name': None, 'diameter': nan, "
              "'hazardous': False})", near_earth_object.__str__())