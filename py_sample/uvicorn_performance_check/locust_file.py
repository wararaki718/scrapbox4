from locust import HttpUser, task, between
    
class IrisUser(HttpUser):
    def on_start(self):
        print("start")

    @task(4) # every running user
    def world(self):
        self.client.post(
            url="/predict",
            headers={"Content-Type": "application/json"},
            json={
                "sepal_length": 0,
                "sepal_width": 0,
                "petal_length": 0,
                "petal_width": 0
            }
        )
    
    def on_stop(self):
        print("stop")
