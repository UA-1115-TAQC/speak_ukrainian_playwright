import os

import allure
import requests
import json


class TestCheckUserDataApi:
    MAXIMUM_RESPONSE_TIME = 1000

    def setup_method(self):
        self.token = self.get_access_token()

    def get_access_token(self):
        response = requests.post(
           "http://speak-ukrainian.eastus2.cloudapp.azure.com/dev/api/signin",
            json={
                "email": os.environ["ADMIN_EMAIL"],
                "password": os.environ["ADMIN_PASSWORD"]
            }
        )
        return response.json()["accessToken"]

    @allure.issue("TUA-375")
    def test_registered_user_can_see_personal_data(self):
        self.send_request_to_check_personal_data()

    def send_request_to_check_personal_data(self):
        response = requests.get(
            "http://speak-ukrainian.eastus2.cloudapp.azure.com/dev/api/user/1",
            headers={"Authorization": f"Bearer {self.token}"}
        )
        assert response.status_code == 200
        user_data = response.json()
        assert user_data["firstName"] == "Admin"
        assert user_data["lastName"] == "Admin"
        assert user_data["phone"] == "0671234567"
        assert user_data["email"] == os.environ["ADMIN_EMAIL"]
        assert user_data["roleName"] == "ROLE_ADMIN"
        assert user_data["urlLogo"] == "/static/images/user/avatar/user1.png"
        assert user_data["status"] == "true"

    def test_check_admin_json_schema(self):
        response = requests.get(
            "http://speak-ukrainian.eastus2.cloudapp.azure.com/dev/api/user/1",
            headers={"Authorization": f"Bearer {self.token}"}
        )
        assert response.status_code == 200
        assert response.json()

        with open("adminJsonSchema.json", "r") as schema_file:
            schema = json.load(schema_file)

        assert response.json() == schema

    def test_response_time_when_checking_personal_data(self):
        response = requests.get(
            "http://speak-ukrainian.eastus2.cloudapp.azure.com/dev/api/user/1",
            headers={"Authorization": f"Bearer {self.token}"}
        )
        assert response.status_code == 200
        assert response.elapsed.total_seconds() * 1000 <= self.MAXIMUM_RESPONSE_TIME
