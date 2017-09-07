#coding=utf-8
import httplib;
import urllib
host = '106.ihuyi.com'
sms_send_uri = '/webservice/sms.php?method=Submit'
account = 'cf_chinamcloud'
password = 'ca0b6b210bb1cf40ec596fe668d925ce668899'
def send_sms(text,mobile):
    params = urllib.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection(host,port=80,timeout=30)
    conn.request("POST",sms_send_uri,params,headers)
    response = conn.getresponse()
    response_str = response.read();
    conn.close()
    return response_str

if __name__ == "__main__":
    mobile = '18612178247'
    text = "您的短信验证码是{}。您的手机号码正在本站进行注册验证，如非本人操作请忽略。".format(556677)
    print send_sms(text,mobile)
