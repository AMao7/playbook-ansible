import time
import requests

page = "http://localhost"
for i in range(1000): 
    requests.get(page) 
    time.sleep(1)
