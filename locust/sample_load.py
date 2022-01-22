from locust import task, constant, HttpUser
from common.csvreader import CSVReader

reader = CSVReader("data/phrases.csv")


class MyLocust(HttpUser):
    api_path = "/stringfinder?pop_size=100&phrase={}"
    wait_time = constant(0)

    @task()
    def prediction_call(self):
        phrase = next(reader)
        print(phrase)
        response = self.client.get(self.api_path.format(phrase[0]))


