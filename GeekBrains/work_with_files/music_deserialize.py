import pickle
import json

with open('group.json', 'r') as f:
    group_json = json.load(f)
    print(group_json)

with open('group.pickle', 'rb') as f:
    group_pickle = pickle.load(f)
    print(group_pickle)

