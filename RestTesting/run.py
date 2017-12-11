import requests
import json
import sys
import os

class bformat:
    HEADER = '\033[95m'
    NEUTRAL = '\033[94m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    CLOSE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Formats used
successfulFormat = bformat.SUCCESS
failureFormat = bformat.FAIL
newTestingFile = bformat.HEADER + bformat.BOLD
endComment = bformat.CLOSE

# "Constants"
execute = 'execute'
given = 'given'
expected = 'expected'
operation = 'operation'

testDirectory = './tests/'
authDirectory = './'

authfile = 'signinauth.json'

# Operations used by requests.
operations = {'GET': (lambda endpoint, request: requests.get(url=endpoint, params=request)),
              'POST':(lambda endpoint, request: requests.post(url=endpoint, data=request)),
              'PUT': (lambda endpoint, request: requests.put(url=endpoint, data=request)),
              'DELETE':(lambda endpoint, request: requests.delete(url=endpoint, data=request)),
              'OPTIONS':(lambda endpoint, request: requests.options(url=endpoint))}


def signin():
    with open(authDirectory + authfile) as authFile:
        auth = json.load(authFile)
        print(auth)

signin()

# Commandline Input
args = sys.argv
testScriptName = args[0]

print("Running ", args[0])

username = args[1] if len(args) > 1 else ""
password = args[2] if len(args) > 2 else ""

# signin auth
def signin(username, password):
    payload = {
        'username': username,
        'password': password
    }

    with requests.Session() as s:
        p = s.post('https://httpbin.org/post', data=payload)
        print(p.text)

        r = s.get('https://httpbin.org/get')
        print(r.text)

# authenticate
if username and password:
    signin(username, password)

#run tests
def run(testFiles):
    for testfile in testFiles:
        print(newTestingFile + "Executing ", testfile + endComment)
        with open(testDirectory + testfile) as rawTests:
            tests = json.load(rawTests)
            executeTests(tests)

def retrieveTestFiles():
    testFiles = [posJson for posJson in os.listdir(testDirectory) if posJson.endswith('.json')]

    return testFiles

def executeTests(tests):
    for endpoint in tests[execute]:
        for test in tests[execute][endpoint]:
            print(test, 'hitting endpoint: ', endpoint)
            request = tests[execute][endpoint][test][given]
            opt = tests[execute][endpoint][test][operation]
            response = operations[opt.upper()](endpoint, request).status_code
            expectedCode = tests[execute][endpoint][test][expected]
            success = (successfulFormat + "PASSED") if response == expectedCode else (failureFormat + "FAILED")
            print('\t' + test, success + bformat.CLOSE, response, 'received, ', expectedCode, "expected ")

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

testDirectory = './tests/'
authDirectory = './'

authfile = 'signinauth.json'

operations = {'GET': (lambda endpoint, request: requests.get(url=endpoint, params=request)),
              'POST':(lambda endpoint, request: requests.post(url=endpoint, data=request)),
              'PUT': (lambda endpoint, request: requests.put(url=endpoint, data=request)),
              'DELETE':(lambda endpoint, request: requests.delete(url=endpoint, data=request)),
              'OPTIONS':(lambda endpoint, request: requests.options(url=endpoint))}