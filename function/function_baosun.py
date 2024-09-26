import requests
import config.config_1


from function.function_tongyong import login
headers=config.config_1.headers_pro

#新增报损总单-订单枚举1成药2中药3参茸4物质赠品
def lossReportingOrder_saveOrUpdate(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/lossReportingOrder/saveOrUpdate"

    headers.update({
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    })
    print(headers)

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re


#新增报损细单商品
def lossReportingOrder_detailSaveOrUpdate(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/lossReportingOrder/detailSaveOrUpdate"

    headers.update({
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    })

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re

#新增报损单送审3,回退送审1
def lossReportingOrder_approve(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/lossReportingOrder/approve"

    headers.update({
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    })

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re


#新增报损单删除
def lossReportingOrder_delete(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/lossReportingOrder/delete"

    headers.update({
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    })

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re

#查询报损单
def lossReportingOrder_page(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/lossReportingOrder/page"

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
    token =login().get("data").get("token")
    b = lossReportingOrder_saveOrUpdate("226831092781060177",token,{
      "groupType": "1",
      "remarks": "自动化测试验证"
    })
    print(b)