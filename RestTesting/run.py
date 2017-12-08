import requests
import json
import sys
import os

# Commandline Input
args = sys.argv
print("Running ", args[0])
if len(args) > 2:
    print("Credentials are missing")
else:
    print("OK")



# Run tests
def run(testFiles):
    for testfile in testFiles:
        print("Executing ", testfile)
        with open(directory + testfile) as rawTests:
            tests = json.load(rawTests)
            executeTests(tests)

# Retrieve test files in the tests directory
def retrieveTestFiles():
    testFiles = [posJson for posJson in os.listdir(directory) if posJson.endswith('.json')]
    return testFiles

# Execute the tests
def executeTests(tests):
    for endpoint in tests[execute]:
        for test in tests[execute][endpoint]:
            print(test, 'hitting endpoint: ', endpoint)
            request = tests[execute][endpoint][test][given]
            opt = tests[execute][endpoint][test][operation]
            operations[opt.upper()](endpoint, request)
        print(test, "Completed")

# Execute script.
testFiles = retrieveTestFiles()
run(testFiles)

# Need to move sign in to file
def signin(user, password):
    # requests.post(data=)
    pass

dict['Applied_poison_rating_bonus'](1, 2)

# Constants
execute = 'execute'
given = 'given'
expected = 'expected'
operation = 'operation'
directory = './tests/'
operations = {'GET': (lambda endpoint, request: print("\tGET", endpoint, request)),
              'POST':(lambda endpoint, request: print("\tPOST", endpoint, request)),
              'PUT': (lambda endpoint, request: print("\tPUT", endpoint, request)),
              'DELETE':(lambda endpoint, request: print("\tDELETE", endpoint, request))}