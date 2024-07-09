# locust_test100.py

import random
from locust import HttpUser, task, between

USER_POOL = [f"user_{i}" for i in range(1, 101)]  # 100 mögliche Benutzer
ASSET_TYPES = ["RohstoffA", "RohstoffB", "RohstoffC", "RohstoffD", "RohstoffE"]

class MyUser(HttpUser):
    wait_time = between(1, 5)
# locust_test100.py    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = None
        self.asset_name = None
# locust_test100.py
    def on_start(self):
        if USER_POOL:
            self.client_id = USER_POOL.pop(random.randint(0, len(USER_POOL) - 1))
            user_number = int(self.client_id.split('_')[1])
            asset_type = ASSET_TYPES[user_number % len(ASSET_TYPES)]
            self.asset_name = f"{asset_type}{user_number}"
        else:
            self.stop(True)  # Stop this user if no more unique IDs are available
# locust_test100.py
    @task(3)
    def post_data(self):
        if not self.client_id:
            return
        payload = {
            "client_id": self.client_id,
            "asset_name": self.asset_name,
            "quantity": random.randint(1, 100),
            "data": {
                "location": random.choice(["Lager A", "Lager B", "Lager C"]),
                "quality": random.choice(["High", "Medium", "Low"])
            }
        }
        self.client.post("/data", json=payload)
# locust_test100.py
    @task
    def get_data(self):
        if not self.client_id:
            return
        self.client.get(f"/data?client_id={self.client_id}")
# locust_test100.py