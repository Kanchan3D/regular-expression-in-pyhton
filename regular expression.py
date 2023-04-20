import re
txt='the rain in spain'
x=re.search("the.*spain",txt)
if x:
    print("yes! we have a match")
else:
    print('no match')


#  ^start
#  .*in betwwen
#   $ end with

import re
txt='the rain in spain'
x=re.search("^the.*spain$",txt)
print(x)
if x:
    print("yes! we have a match")
else:
    print('no match')