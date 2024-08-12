import requests
import config.config_1


from function.function_tongyong import login

#新增调拨总单
def allotOrder_save(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/allotOrder/save"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re


#新增调拨细单商品
def allotOrderDetail_modify(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/allotOrderDetail/modify"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re

#调拨送审
def allotOrder_submit(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/allotOrder/submit"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re


#调拨校验是否可以以调拨

def allotOrderDetail_check(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/allotOrderDetail/check"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re



#作废调拨单
def allotOrder_disable(departmentid,token):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/allotOrder/disable"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,

        "sl-mode-department-id":departmentid
    }
    data={
  "allotOrderId": "367429180268085248"
}
    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re




if __name__ == '__main__':
    token=login().get("data").get("token")
    print(token)
    b = allotOrderDetail_check("226831268358819992",token,{'producingBatchNumber': '385230351', 'allotObjId': '373543393204727808', 'goodsId': '179094728321556481', 'departmentId': '226831268358819992'})
    print(b)