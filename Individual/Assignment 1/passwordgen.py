from lib2to3.pygram import Symbols
import string
lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
num = list(string.digits)
symbols = list(string.punctuation)
 
all = lower + upper    + num   + symbols
import datetime
password =" "
for _ in range(1,12):  #just use underscore for variable if it does not 
    
    now = datetime.datetime.now().microsecond
    # print(now)

    now2= list(str(now))
    # print(now2)

    # print(all[int(now2[0])])
    
    password += all[int(now2[-1])]
print(password)