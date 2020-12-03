from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
client = AcsClient('LTAI4FzXq4ZMvHqsG89UX51W', 'gVL3IaGTqrkqJmffYbgtHbQvzG602w', 'cn-hangzhou')

def send_sms(phonenumber,code):
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', phonenumber)
    request.add_query_param('SignName', "")
    request.add_query_param('TemplateCode', "SMS_206470102")
    request.add_query_param('TemplateParam', "{\"code\":\"%s\"}" % code)

    response = client.do_action(request)
    # python2:  print(response)
    print(str(response, encoding='utf-8'))

