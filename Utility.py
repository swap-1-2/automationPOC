import json
import unittest
from unittest import TestCase, main

import jsonschema as jsonschema
import requests
import Constants

def validate_Status_Code(self,url):
    # define api response
    testurl = (url)
    text="## Checking status code for %s ##" %(testurl)
    print (text)
    response = requests.get(testurl)
    # read response
    html = response.json()
    # assert response
    self.assertTrue(response.status_code == requests.codes.ok)


def validate_Json_Schema(self,url,jsonPath):

        text = "## Checking JSON schema for %s ##" % (url)
        print(text)
        # define api response
        testurl = (url)
        #Validate json schema
        response = requests.get(testurl)
        json_data = response.json()
        with open(jsonPath, 'r') as f:
            schema_data = f.read()
        schema = json.loads(schema_data)
        jsonschema.validate(json_data, schema)