## API Automation using Python
This is automation framework for Rest API /albulms and /Usres

Prerequisites:
The framework requires packages to be installed with pycharm IDE 
1) json
2) unittest
3) jsonschema
4) requests
5) xmlrunner
6) Constants
7) Utility

## Usage

C:\Users\xyz\PycharmProjects\POC> python -m unittest restAPIAutomation.py Constants.py Utility.py

.Checking JSON schema for https://jsonplaceholder.typicode.com/albums 
0.3325035572052002
 .Checking JSON schema for https://jsonplaceholder.typicode.com/users 
0.08449840545654297
 .Checking status code for https://jsonplaceholder.typicode.com/albums 
0.07399821281433105
 .Checking status code for https://jsonplaceholder.typicode.com/users 
0.09149956703186035
.
----------------------------------------------------------------------
Ran 4 tests in 0.604s

OK


## More Information:
It has

1) JsonSchema directory : For json schema file
2) Constants.py : for keeping all test data
3) restAPIAutomation.py : for test cases functions
4) Utility.py : for keeping all reusable functions
