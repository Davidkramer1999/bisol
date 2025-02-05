import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "http://localhost:80")

customer = "customer00"
start_time = "2024-01-01T00:00:00"
end_time = "2024-01-01T01:00:00"


def test_get_energy_data():
    url = (
        f"{BASE_URL}/energy/user/{customer}?start_time={start_time}&end_time={end_time}"
    )
    response = requests.get(url)
    print(response.json())


def test_calculate_costs_revenues():
    url = f"{BASE_URL}/energy/user/{customer}/calculate?start_time={start_time}&end_time={end_time}"
    response = requests.get(url)
    print(response.json())


if __name__ == "__main__":
    test_get_energy_data()
    test_calculate_costs_revenues()
