import json
from pprint import pprint


with open('values.json', 'r', encoding='utf-8') as f_1:
    data_1 = json.load(f_1)


with open('tests.json', 'r', encoding='utf-8') as f_2:
    data_2 = json.load(f_2)


for t in data_2['tests']:
    for v in data_1['values']:
        if int(t['id']) == int(v['id']):
            t['value'] = v['value']


for t in data_2['tests'][2]['values']:
    for v in data_1['values']:
        if int(t['id']) == int(v['id']):
            t['value'] = v['value']


for t in data_2['tests'][2]['values'][0]['values'][0]['values']:
    for v in data_1['values']:
        if int(t['id']) == int(v['id']):
            t['value'] = v['value']


for t in data_2['tests'][2]['values'][1]['values'][0]['values']:
    for v in data_1['values']:
        if int(t['id']) == int(v['id']):
            t['value'] = v['value']


for t in data_2['tests'][3]['values']:
    for v in data_1['values']:
        if int(t['id']) == int(v['id']):
            t['value'] = v['value']

pprint(data_2)


with open('report.json', 'w', encoding='utf-8') as new_report:
    json.dump(data_2, new_report, ensure_ascii=False)





# def write_report(data, filename="report.json"):
#     with open (filename, 'w') as report:
#         json.dump(data, report, indent=4)
#
# with open('report.json') as new_report:
#     data = json.load