from locust import HttpUser, task, between

class EventsUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        # Set reusable params once
        self.user_param = {"user": "locust_user"}
        self.headers = {
            "Accept": "text/html"
        }

    @task
    def view_events(self):
        self.client.get(
            "/events",
            params=self.user_param,
            headers=self.headers
        )