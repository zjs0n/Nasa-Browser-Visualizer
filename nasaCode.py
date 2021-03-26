import json
data = {}
data['launches'] = []
data['launches'].append({
    'name': 'Bear I',
    'original_date': 'April 1 ',
    'changed_date': ''
})
data['launches'].append({
    'name': 'Orca I',
    'original_date': 'April 3',
    'changed_date': 'April 12'
})
data['launches'].append({
    'name': 'Moose I',
    'website': 'April 5',
    'from': 'April 5'
})
data['launches'].append({
    'name': 'Bear II',
    'website': 'April 10',
    'from': 'April 10'
})
data['launches'].append({
    'name': 'Bumblebee I',
    'website': 'April 12',
    'from': 'April 16'
})
data['launches'].append({
    'name': 'Bumblebee II',
    'website': 'April 13',
    'from': 'April 17'
})
data['launches'].append({
    'name': 'Bumblebee III',
    'website': 'April 14',
    'from': ''
})
data['launches'].append({
    'name': 'Bumblebee IV',
    'website': 'April 15',
    'from': ''
})
data['launches'].append({
    'name': 'Orca II',
    'website': 'April 20',
    'from': 'April 20'
})
data['launches'].append({
    'name': 'Moose II',
    'website': 'April 23',
    'from': 'April 23'
})
data['launches'].append({
    'name': 'Bear III',
    'website': 'April 30',
    'from': 'April 30'
})

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)
