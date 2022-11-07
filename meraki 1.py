#Q.1 Json data ko python object main convert karne ka program likho?.

import json
j='{"name":"jeyesh","city":"kannod","year":2020}'
p=json.loads(j)
print(p)
print(type(p))