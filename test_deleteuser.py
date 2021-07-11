import requests
import pytest


class Test_deleteapi:
    def test_delete(self):
        response = requests.delete("https://reqres.in/api/users/2", timeout=2)
        print(response)
        assert response.status_code == 204, "User Deletion failed"



