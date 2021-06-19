from datetime import datetime
import json

current = datetime.utcnow()

# dt_json = json.dumps(current)
# print(dt_json)

def format_iso(dt):
    return dt.strftime('%Y-%m-%dT%H:%M:%S')