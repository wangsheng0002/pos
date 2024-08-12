'''环境配置'''

# 生产环境域名
import time

#测试环境
url_pro = "https://dslpos-api-test.dslbuy.com"


#生产环境
# url_pro = "https://dslpos-api.dslyy.com"



# #登录账号密码用户-测试
data_user={
  "loginName": "18070490002",
  "verifyCodeKey": "",
  "verifyCode": "",
  "password": "tnEpg7bt6YFouExm2ZShF/toY0IDNyRzqKVmgI7fO8kYDYo4BECI7Gv4YWdvLSg6nGNAGIdzk/uhR5iE4nvsAdVqD4GBQ27USL295G7tCJhDMNFSU+kT09QC85zdyEquK/BDNJiRSWv6W6qm8NRXYJ1DiHvKtVMBIZiJ26Zn62k=",
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



# 请求头
headers_pro = {
    "Content-Type": "application/json",
    "token":""

}