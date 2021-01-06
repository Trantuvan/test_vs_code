import math
import sys
from os import rename

import requests

print(sys.version)
print(sys.executable)


def greet(who_are_you):
    greeting = "Hello, {}".format(who_are_you)
    return greeting


r = requests.get("https://coreyms.com")
print(r.status_code)
