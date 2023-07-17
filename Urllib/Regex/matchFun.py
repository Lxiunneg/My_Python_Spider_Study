import re

content1 = '2022-12-22 13:23'

pattern = re.compile('\d{2}:\d{2}',re.S)

result = re.sub(pattern,'',content1)
print(result)
