import json

d1 = {'a': 100, 'b': 200}

d1_json = json.dumps(d1)

print(json.dumps(d1, indent=2))