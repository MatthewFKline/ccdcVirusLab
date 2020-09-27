#!/usr/bin/python3

from flask import Flask, request
import redis
import json
import time

app = Flask(__name__)

machineCount = 50 # PSA: This doesn't affect the display, just when the update requests loop back to 0
virusCount = 5

@app.route('/api/submit')
def addJob():
    id = request.args.get('id')
    virusName = request.args.get('virusName')
    timestamp = time.time()
    r = redis.StrictRedis(host='localhost', port=6379) #renamed redis -> localhost
    r.rpush(id, json.dumps({'timestamp': timestamp,
                            'virusName': virusName}))
    return 'Saved'

@app.route('/api/getDeltaTime')
def getDeltaTime():
    id = request.args.get('id')
    virusName = request.args.get('virusName')
    if request.args.get('jsonp'):
        return request.args.get('jsonp') + "(" + getDeltaTimeFromRedis(id, virusName) + ")"
    return getDeltaTimeFromRedis(id, virusName)

def getDeltaTimeFromRedis(id, virusName):
    r = redis.StrictRedis(host='localhost', port=6379) #renamed redis -> localhost
    data = [json.loads(x.decode('utf-8')) for x in r.lrange(id, 0, -1) if json.loads(x.decode('utf-8'))['virusName'] == virusName]
    if len(data) > 0:
        min = data[0]
        for datum in data[1:]:
            if datum['timestamp'] > min['timestamp']:
                min = datum
        timeDiff = str(time.time() - min['timestamp'])
        return timeDiff
    return "0.0"  # Default virus?

@app.route("/")
def getSlash():
    with open('index.html') as f:
        index = f.read()
    machineHTML = ""
    for machineIndex in range(machineCount):
        machineHTML += "<div class=\"item\"><h2>Machine %s</h2>" % machineIndex
        for virusIndex in range(virusCount):
            machineHTML += """<div class="" id="Machine%s_Virus%s" style="background: #26a815"><center>Virus%s</center></div>\n<br>\n""" % (machineIndex, virusIndex, virusIndex)
        machineHTML += "</div>"
    functions = ""
    interval = "setInterval(function() {"
    for machineIndex in range(machineCount):
        for virusIndex in range(virusCount):
            functions += """function setColor%s%s(delay) {setColor(delayToColor(delay),%s,%s);};\n""" % (machineIndex, virusIndex, machineIndex, virusIndex)
            interval += """addScript('/api/getDeltaTime?id=%s&virusName=%s&jsonp=setColor%s%s');""" % (machineIndex, virusIndex, machineIndex, virusIndex)
    interval += "}, 5000);"
    return index.replace('REPLACEME_BOXES', machineHTML).replace('REPLACEME_SCRIPT', functions + interval)


app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
