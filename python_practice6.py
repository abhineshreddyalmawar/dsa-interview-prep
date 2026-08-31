# PHASE A - DAY 4 (Jul 29, 2026) | File & JSON Handling
# Real-world tie-in: NexusAI - loads() for receiving GitHub MCP data, dumps() for sending email/API reports

import json

# --- json.loads() : JSON text (str) -> Python dict ---
raw_json = '{"city": "Newark", "population": 311000}'   # double quotes inside -> this is JSON text (str)
print(type(raw_json))              # <class 'str'>

data = json.loads(raw_json)
print(data)                        # {'city': 'Newark', 'population': 311000} -> single quotes = Python printed a real dict
print(type(data))                  # <class 'dict'>
print(data["city"])                # Newark -- normal dict access now works

# --- json.dumps() : Python dict -> JSON text (str), reverse direction ---
# Input can be written with EITHER quote style -- Python treats them identically:
city_info = {'city': 'Newark', 'population': 311000}    # OR {"city": "Newark", ...} -- SAME dict either way

text_version = json.dumps(city_info)
print(text_version)                # {"city": "Newark", "population": 311000} -- ALWAYS double quotes (JSON standard)
print(type(text_version))          # <class 'str'>

# --- THE RULE, one line ---
# JSON text (str)     -> double quotes    (raw_json above, and dumps() output)
# Python dict          -> single quotes    (how Python prints a real dict, e.g. `data` above)
# Quote style YOU choose when writing your own dict in code = irrelevant, Python treats ' and " the same.
# Only json.dumps() output is FORCED to double quotes -- that's the JSON standard, not a Python styling choice.