import requests
import config.config_1


from function.function_tongyong import login

#查询收货列表总单
def acceptOrder_page(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/acceptOrder/page"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }

    re=requests.get(url=url,params=data,headers=headers).json()
    #返回post请求结果
    return re
#查询收货列表细单
def acceptOrderDetail_page(departmentid,token):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/acceptOrderDetail/page"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }
    data= {
      "pageNum": 1,
      "pageSize": 60,
      "distributeOrderId": "367150252519825408",
      "loadTmc": True
    }
    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re





#整单收货
def acceptOrder_accept(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/acceptOrder/accept"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re

#细单收货
def acceptOrder_acceptDetail(departmentid,token):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/acceptOrder/acceptDetail"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }
    data={
      "id": "367150253035724800"
    }
    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re







if __name__ == '__main__':
    token = login().get("data").get("token")
    b = acceptOrder_page("226831092864946234",token)
    print(b)