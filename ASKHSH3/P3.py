import re
FILENAME = 'P3file.cpp'

with open(FILENAME) as myFile:
  text = myFile.read()

regex_sc = r'//(.*)'
regex_mc = r'/\*( .*\s.* )\*/'


list_single = re.findall(regex_sc,text)
for comment, count in enumerate(list_single, 1):
  print("SingleLine Comment", comment, ": ", count, '\n')


print('\n','\n','\n')


list_multi = re.findall(regex_mc, text)
for comment, count in enumerate(list_multi, 1):
    print("MultiLine Comment", comment, ": ", count, '\n')