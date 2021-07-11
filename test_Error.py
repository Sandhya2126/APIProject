import requests

class Test_apierror:
    def test_errocode(self):
        response = requests.get("https://dummy.restapiexample.com/public/api/v1/update/21", timeout=2)
        print(response)
        response_code = response.status_code
        assert response_code == 200, "Response Code doesn't match"
        json = response.json()
        print(json)
