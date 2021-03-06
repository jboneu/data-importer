#!/usr/bin/env python3

import os
import sys
import json
from jinja2 import Template

name = "history.json"

#if sends an argument first argument is filename. by default history.json
if len(sys.argv) > 1:
    name = sys.argv[1]

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = dir_path + "/" + name
filename = '/extra/data.json'

with open(filename, "r") as lines:
    for line in lines:
        #data = json.load(json_file)
        #after longitude there are 4 values to understand | gpsAge | speedKPH | heading | altitude |
        #differences between time and lastgps_time
        template_line = "INSERT INTO `EventData` VALUES ('{{account}}','{{device}}',{{time.epoch_time}},{{deviceData.gpsdata.event}},{{deviceData.gpsdata.latitude}},{{deviceData.gpsdata.longitude}},10,{{deviceData.gpsdata.speed}},{{deviceData.gpsdata.heading}},{{deviceData.gpsdata.altitude}},'',0,0,0,'{{deviceData.gpsdata.address}}','','',{{deviceData.distanceDelta|default(0,true)}},{{deviceData.mileage|default(0,true)}},0,0,'',{{time.epoch_time}},'','','','','','',0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,'',0,'',0,'',0,0,0,'','','','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'',0,0,0,0,0,0,0,0,0,0,0,0,0,0,'',0,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'',0,0,0,'','','','','','') ON DUPLICATE KEY UPDATE timestamp = timestamp;"
        #template_line = "$vehicle ... $account ... $time.epoch_time"
        tm = Template(template_line)
        #print(line)
        item = json.loads(line)
        result = tm.render(item)
        print(result)
