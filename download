import requests
import json
import time,sys
url = "http://192.168.1.1/"
#data是post要提交的数据，里面包含了密码
data = json.dumps({"method": "do", "login": {"password": "0KcgeXhc9TefbwK"}})
response = requests.post(url,data=data)
#stok 是提交登陆指令后返回的身份令牌，相当于cookies，之后的url加上stok才有权限
stok = json.loads(response.text).get("stok")

url = 'http://tplogin.cn/stok='+stok+'/ds'
#下面的data用于post“当前在线列表”的请求
data = json.dumps({"hosts_info": {"table": "online_host"}, "method": "get"})
response = requests.post(url,data)



#下面的都是分析

#print(response.encoding)
#response.encoding = response.apparent_encoding

#将返回的json转换成python数据类型
responseDict = json.loads(response.text)
#print(responsedict)
#从数据中提取主机信息
hosts_info = (responseDict.get("hosts_info"))
#print(hosts_info)
#从主机中提取在线列表
online_host = hosts_info.get("online_host")
#print(online_host)
print()
#下面列表用于存储mac
macList = []

#下面循环用于将mac添加进入列表
for hostinfo in online_host:
    for key in hostinfo:
        macList .append(hostinfo[key].get("mac"))
        #下面一条显示，没啥用
        print("hostname :" ,hostinfo[key].get("hostname"),"   mac :" ,hostinfo[key].get("mac"),"    ip:" ,hostinfo[key].get("ip"),)
#获取当前时间
currentTime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

#用当前时间与mac列表构成字典，用于输出json
result = {currentTime:macList}

#下面输出
with open("f:\\json\\time.json",'a+')as f:
    json.dump(result,f)
    f.write("\n")
f.close()
