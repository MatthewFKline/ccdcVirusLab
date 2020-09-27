import os
import requests
import time
from sys import argv

def taunt():
    #os.system('wall "Taunt..."')
    pass

def update():
    requests.get('http://68.183.100.83:8080/api/submit?id=%s&virusName=0' % argv[1])
    requests.get('http://68.183.100.83:8080/api/submit?id=%s&virusName=1' % argv[1])
    requests.get('http://68.183.100.83:8080/api/submit?id=%s&virusName=2' % argv[1])
    requests.get('http://68.183.100.83:8080/api/submit?id=%s&virusName=3' % argv[1])
    requests.get('http://68.183.100.83:8080/api/submit?id=%s&virusName=4' % argv[1])

while True:
    taunt()
    update()
    time.sleep(5)
