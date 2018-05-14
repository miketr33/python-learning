import re

myRegex = re.compile('\d{2,3}')
mo = myRegex.search("120_Bm_Byfilenamingchecker_01.wav and 79_another")
if mo is not None:
    print(mo.group())
