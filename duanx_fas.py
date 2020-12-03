from DuanXin.ali_sms import send_sms
import string
import random
#这个方法专门用来生成字母加数字

def get_code(number):
    source = list(string.ascii_letters) #成一个 大写字母小写字母的列表
    for x in range(0,10):
        source.append(str(x)) # 把0-9混进去
    return "".join(random.sample(source,number))

send_sms(phone,get_code(5))
