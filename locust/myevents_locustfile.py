from locust import HttpUser, task, between

class MyEventsUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        # Reuse static request data instead of recreating it every request
        self.user_param = {"user": "locust_user"}
        self.headers = {
            "Accept": "text/html"
        }

    @task
    def view_my_events(self):
        self.client.get(
            "/my-events",
            params=self.user_param,
            headers=self.headers
        )