from datetime import datetime

import requests
import config.config_1


from function.function_tongyong import login
headers=config.config_1.headers_pro
#查询开启批次门店
def getStoreBatchConfigPage(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/batchConfig/getStoreBatchConfigPage"

    headers.update({
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    })

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re

#查询开启批次营运区
def getRegionBatchConfigPage(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/batchConfig/getRegionBatchConfigPage"

    headers.update({
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    })

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re



if __name__ == '__main__':
    print(datetime.now().strftime("%Y-%m-%d 00:00:00"))

    token =login().get("data").get("token")
    b = getRegionBatchConfigPage("1",token,{
  "pageNum": 1,
  "pageSize": 60
})
    print(b)