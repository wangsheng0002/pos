import requests
import config.config_1


from function.function_tongyong import login

#新增请货总单
def returnOrder_save(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/returnOrder/save"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re


#新增退货细单商品
def returnOrderDetail_modify(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/returnOrderDetail/modify"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re

#新增退货单送审1,回退送审2
def returnOrder_sendApprove(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/returnOrder/sendApprove"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re


#新增退货单删除
def returnOrder_del(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/returnOrder/delete"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re


#退货检查
def returnOrderDetail_check(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/returnOrderDetail/check"

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
    b = returnOrderDetail_check("226831092781060177",token,1)
    print(b)