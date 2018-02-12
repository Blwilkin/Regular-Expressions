import re

atRegex = re.compile(r'cat')
bo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(bo)