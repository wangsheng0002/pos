import requests
import config.config_1


from function.function_tongyong import login

#新增报溢总单
def inventoryOverflow_add(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/inventoryOverflow/add"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re


#新增报溢细单商品
def inventoryOverflow_detail(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/inventoryOverflow/detail"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re

#新增报溢送审3,回退送审1,审批通过5，审批不通过7
def inventoryOverflow_updateState(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/inventoryOverflow/updateState"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re


#新增报溢单删除
def inventoryOverflow(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/inventoryOverflow"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }

    re=requests.delete(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re


#查询报溢单
def inventoryOverflow_page(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/inventoryOverflow/page"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }

    re=requests.get(url=url,params=data,headers=headers).json()
    #返回post请求结果
    return re





if __name__ == '__main__':
    token =login().get("data").get("token")
    b = inventoryOverflow_page("226831092781060177",token,{
  "pageNum": 1,
  "pageSize": 60
})
    print(b)