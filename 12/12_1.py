def parse_dict(data):
    data_sum = 0

    if isinstance(data, list):
        for i in data:
            data_sum += parse_dict(i)
    elif isinstance(data, dict) and 'red' not in data.values():
        for i in data:
            data_sum += parse_dict(data[i])
    elif isinstance(data, int):
        data_sum += data

    return data_sum

import json

input_file = open('input.txt').read()
data = json.loads(input_file)

print parse_dict(data)
