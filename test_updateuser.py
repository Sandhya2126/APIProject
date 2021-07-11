import requests
import pytest

class Test_putapi:
    def test_update(self):
        payload = {
            "name": "Ms. Sandhya",
            "job": "Automatoion Tester"
        }
        response = requests.put("https://reqres.in/api/users/2", data=payload, timeout=3)
        print(response)
        print(response.json())



