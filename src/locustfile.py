from locust import HttpUser, task, between, constant
from requests import Response


class UserBehavior(HttpUser):
    """
    see.
    http://docs.locust.io/en/stable/writing-a-locustfile.html#writing-a-locustfile
    """

    @task
    def sample(self):
        pass

        """
        #############
        sample code
        #############


        url = "/test"

        headers = {
            "Content-Type": "application/json"
        }

        data = {
            "data": "dummy"
        }

        req: Response = self.client.post(
            url=url,
            headers=headers,
            json=data)

        """
