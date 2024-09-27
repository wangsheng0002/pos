'''环境配置'''

# 生产环境域名
import csv
import time

#生产环境
# url_pro = "https://dslpos-api.dslyy.com"


def read_csv(filename):

    filenames = '../data/'+filename
    with open(filenames, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        #创建列表保存CSV数据
        list_csv=[]
        for row in csvreader:
            # 遍历csvreader对象的每一行内容并保存
            list_csv.append(row)
    return list_csv

lists = read_csv("测试.csv")
print(lists)
for i in lists:
    if i[0] == "url":
        url=i[1]
        if "test" in url:
            sl_role=0
        else:
            sl_role = 2
    if i[0] == "phone":
        phone=i[1]
    if i[0] == "password":
        password=i[1]
    if i[0] == "env":
        env=i[1]

#测试环境
url_pro = url

# 请求头
headers_pro = {
    "Content-Type": "application/json",
    "token":"",
    "env":env,
    "sl-role": sl_role

}

# #登录账号密码用户-测试
data_user={
  "loginName": phone,
  "verifyCodeKey": "",
  "verifyCode": "",
  "password": password,
  "appId": 1
}



#登录账号密码用户-生产
# data_user={
#   "loginName": "18070490002",
#   "verifyCodeKey": "",
#   "verifyCode": "",
#   "password": "LLO8JMDt+iMe3z8e11UPgH57P+HVmnL68EDDU1LZ84/ego6ad54htvrvLGHeZifK1lvw8lbQpaSNpnqhDVGsp7gFq6Xsf/EEG6VF1q87mJf0784llcstnZaPCcHAyuQlD/XuVmPPuXGVo2MZCcA7oO6XiFR+0673mcnQrtJWcZk=",
#   "appId": 1
# }

# #登录验证码用户
# data_user={
#   "phone": "18070490002",
#   "phoneCode": "123456",
#   "appId": 1,
#   "verifyCodeKey": int(time.time())
# }



