import json
from collections import defaultdict

with open(r"C:\Users\User\Desktop\f\tests.json") as f:
    tests_json = json.load(f)
    
with open(r"C:\Users\User\Desktop\f\values.json") as f:
    values_json = json.load(f)

def reccurent_find_value(tests: dict, test_id: int, value_set):
    # ищем тест без value
    for test in tests:
        if test['id'] is test_id:
            test['value'] = value_set
            return
        if 'values' in test:
            reccurent_find_value(test['values'], test_id, value_set)
    return


for item in values_json['values']:
    value_test_id = item['id']
    value = reccurent_find_value(tests_json['tests'], value_test_id, item['value'])


with open('report.json', 'w') as f:
    print(json.dump(tests_json, f, indent=4))