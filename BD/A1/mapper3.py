#!/usr/bin/python
import json
import sys
for line in sys.stdin:
 
    tuple=json.loads(line.strip())
    if tuple:
      date=tuple["timestamp"].strip()
      location=int(tuple["location"])
      sensor_id=int(tuple["sensor_id"])
      pressure=float(tuple["pressure"])
      humidity=float(tuple["humidity"])
      temp=float(tuple["temperature"])
	  
      if (location<2500) and (location>1700) and (sensor_id<5000) and (pressure>=93500) and (humidity>=72.00) and (temp>=12):
        #print(f"{date}\t1")
        print('%s\t%s' % (date,1))
  
