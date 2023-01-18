#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter, and
finally displays the body of the response."""

import requests
import sys

if __name__ == '__main__':

    new_value = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], new_value)
    print(req.text)
