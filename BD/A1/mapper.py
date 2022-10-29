#!/usr/bin/env python3


import json 
import sys
import math

output = ""

for line in sys.stdin:
    try :
        json_obj = json.loads(line.strip())
    except:
        continue
    location = int(json_obj["location"])
    if location > 1700 and location < 2500 and math.isnan(location) == False:
        sensor_id = int(json_obj["sensor_id"])
        if sensor_id < 5000 and math.isnan(sensor_id) == False:
            pressure = float(json_obj["pressure"])
            if pressure >= 93500.00 and math.isnan(pressure) == False:
                humidity = float(json_obj["humidity"])
                if humidity >= 72.0 and math.isnan(humidity) == False:
                    temperature = float(json_obj["temperature"])
                    if temperature >= 12.00 and math.isnan(temperature) == False: 
                        timestamp = json_obj["timestamp"]
                        output+=timestamp+"\n"
print(output)

