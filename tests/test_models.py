import unittest

from models import NearEarthObject, CloseApproach


class TestModels(unittest.TestCase):

    def test_object_initialized_by_NearEarthObject_model(self):

        near_earth_object = NearEarthObject('designation_value', 'iau_name_value', 'diameter_value', True)
        self.assertEqual("NearEarthObject({'designation': 'designation_value', 'iau_name': 'iau_name_value', "
                         "'diameter': 'diameter_value', 'hazardous': True})", near_earth_object.__str__())

    def test_edge_cases_by_initialization_of_NearEarthObject_model(self):
        near_earth_object = NearEarthObject('designation_value')
        print("NearEarthObject({'designation': 'designation_value', 'name': None, 'diameter': nan, "
              "'hazardous': False})", near_earth_object.__str__())