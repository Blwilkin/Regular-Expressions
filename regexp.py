import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

atRegex = re.compile(r'.at')
bo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(bo)