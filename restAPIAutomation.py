import json
import unittest
import time
from unittest import TestCase, main
#import HtmlTestRunner
import jsonschema as jsonschema
import requests
import xmlrunner as xmlrunner
import Constants
import Utility


class RestApiTestSmokeTest(TestCase):
    def setUp(self):
        self.startTime = time.time()

    def test_Status_code_for_Users(self):
        Utility.validate_Status_Code(self,Constants.UsersApiUrl)

    def test_Status_code_for_Albums(self):
        Utility.validate_Status_Code(self,Constants.AlbumApiUrl)

    def test_Json_Schema_Users(self):
        Utility.validate_Json_Schema(self,Constants.UsersApiUrl,Constants.UsersJsonSchema)

    def test_Json_Schema_Albums(self):
        Utility.validate_Json_Schema(self,Constants.AlbumApiUrl,Constants.AlbumJsonSchema)

    def tearDown(self):
        t = time.time() - self.startTime
        print (t)

if __name__ == "__main__":
    # Create XMLTestRunner object and run the test suite.
    test_runner = xmlrunner.XMLTestRunner(output="test_reports")
    test_suite = unittest.TestSuite()
    test1 = unittest.makeSuite(RestApiTestSmokeTest)
    test_runner.run(main)
