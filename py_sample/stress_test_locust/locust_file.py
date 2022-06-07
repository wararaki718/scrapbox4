from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello(self):
        self.client.get("/hello")
    
    @task
    def world(self):
        self.client.get("/world")
