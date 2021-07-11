import requests
import pytest

class Test_postapi:
    def test_create(self):
        payload = {
            "name": "Sandhya Negi",
            "job": "Python Automatoion Tester"
        }
        response = requests.post("https://reqres.in/api/users", data=payload, timeout=4)
        print(response)
        print(response.json())


