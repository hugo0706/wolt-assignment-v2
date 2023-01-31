import json
import os
def read_test_data():
    path =  os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test_data.json')
    
    with open(path) as f:
        data = json.load(f)        
    return data
