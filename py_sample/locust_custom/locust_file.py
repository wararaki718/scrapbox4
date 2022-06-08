from locust import HttpUser, task, between

class HelloUser(HttpUser):
    @task
    def hello(self):
        self.client.get("/hello")
    
class WorldUser(HttpUser):
    def on_start(self):
        print("start")

    @task(5) # every running user
    def world(self):
        self.client.get("/world")
    
    def on_stop(self):
        print("stop")
    
    wait_time = between(0.5, 5)
    weight = 3

