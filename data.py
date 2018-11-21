from random import seed, shuffle
import numpy as np
import time
import json

# global 
DATA_SIZE = 64

''' Random set '''
seed(time.time())
nums = list(range(1, DATA_SIZE+1))
shuffle(nums)
colors = [(0, 0.5 + n/(2*DATA_SIZE), 1 - n/(2*DATA_SIZE), 1) for n in nums]
data = [[nums[i], colors[i]] for i in range(len(nums))]

fo = open("random_data.json", "w")
json.dump(obj=data, fp=fo)

''' Decending set '''
nums = list(range(DATA_SIZE, 0, -1))
colors = [(0, 0.5 + n/(2*DATA_SIZE), 1 - n/(2*DATA_SIZE), 1) for n in nums]
data = [[nums[i], colors[i]] for i in range(len(nums))]

fo = open("decending_data.json", "w")
json.dump(obj=data, fp=fo)

''' Read data '''
# fr = open("random_data.json")
# raw_data = json.load(fp=fr)
# print(raw_data)