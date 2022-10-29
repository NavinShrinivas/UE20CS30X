#!/usr/bin/env python3

from kafka import KafkaConsumer
import sys
import json

topic = sys.argv[1]
consumer = KafkaConsumer(topic)
state_count = dict()
state_min_max = dict()
for message in consumer:
    if message.value.decode() == "EOF\n" or message.value.decode() == "EOF":
        answer = dict()
        for k in sorted(state_min_max):
            answer[k] = dict()
            answer[k]["Min"] = round(float(state_min_max[k]["Min"]/state_count[k]),2)
            answer[k]["Max"] = round(float(state_min_max[k]["Max"]/state_count[k]),2)
        print(json.dumps(answer, indent=4), end="")
        sys.exit()
    message_split = message.value.decode().split(",")
    try : 
        state_count[message.key.decode()] += 1
        state_min_max[message.key.decode()]["Min"] += float(message_split[0])
        state_min_max[message.key.decode()]["Max"] += float(message_split[1])
    except: 
        state_count[message.key.decode()] = 1
        state_min_max[message.key.decode()] = dict()
        state_min_max[message.key.decode()]["Min"] = float(message_split[0])
        state_min_max[message.key.decode()]["Max"] = float(message_split[1])
