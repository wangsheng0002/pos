import requests
import config.config_1


from function.function_tongyong import login

#新增请货总单
def requestOrder_save(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/requestOrder/save"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re


#新增请货细单商品
def requestOrderDetail_modify(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/requestOrderDetail/modify"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re

#新增请货单送审1,回退送审0
def requestOrder_submit(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/requestOrder/submit"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re


#新增请货单删除
def requestOrder_del(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/requestOrder/del"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re

#查询请货总单
def requestOrder_del(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/requestOrder/del"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re







if __name__ == '__main__':
    token =login().get("data").get("token")
    b = requestOrder_del("226831092781060177",token,371531724992618496)
    print(b)