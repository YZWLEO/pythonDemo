#coding=utf-8
import m524sms;

mobile = '18612178247'
text = "您的短信验证码是{}。您的手机号码正在本站进行注册验证，如非本人操作请忽略。".format(889900)
string = m524sms.send_sms(text,mobile)
print string;


