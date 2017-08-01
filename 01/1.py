import random
import string
import pprint
# from random import *
def new_activation(n):
    choice_list = list(string.lowercase) + list(string.uppercase) + [str(i) for i in range(0,10)]
    string_temp = []
    for i in xrange(n):
        temp_string = random.choice(choice_list)
        string_temp.append(temp_string)
    string_temp = "".join(string_temp)
    return string_temp

activa_list = []
for i in range(2):
    activa_list.append(new_activation(110))

pprint.pprint(activa_list)