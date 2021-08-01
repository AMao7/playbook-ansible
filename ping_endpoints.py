import time
import requests
import random

def successful_ping():
    page = "http://localhost"
    random_request = random.randint(10, 100)    
    for i in range(random_request):
        requests.get(page)
        time.sleep(1)

def unsuccessful_ping():
    page = "http://localhost/error!!!!!"
    random_request = random.randint(10, 100)    
    for i in range(random_request):
        requests.get(page)
        time.sleep(1)
while True:        
  successful_ping()
  unsuccessful_ping()



