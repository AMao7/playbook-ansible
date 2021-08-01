import time
import requests
import random

def successful_ping():
    page = "http://localhost"
    random_request = random.randint(1000, 10000)    
    for i in range(random_request):
        requests.get(page)
        time.sleep(1)

def unsuccessful_ping():
    page = "http://localhost:1"
    random_request = random.randint(1000, 10000)    
    for i in range(random_request):
        requests.get(page)
        time.sleep(1)
while True:        
  successful_ping()
  unsuccessful_ping()



