import csv
import time
import os


import requests
import config.config_1
headers=config.config_1.headers_pro
'''读csv文件并按返回列表'''
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


'''写入结果到csv文件'''

def writ_csv(list_csv,filename):
    filenames = '../data/'+filename
    with open(filenames, "w",newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in list_csv:
            # 遍历csvreader对象的每一行内容并写入
            writer.writerow(row)
    return list_csv



# #登录验证码登录
# def login():
#     #引用配置的域名
#     url = config.config_1.url_pro+"/api/sl-authorization/v1/phoneCodeLogin"
#
#     data = config.config_1.data_user
#     re=requests.post(url=url, json=data).json()
#     #返回post请求结果
#     return re

#登录账号密码登录
def login():
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-authorization/v1/login"

    data = config.config_1.data_user

    re=requests.post(url=url,json=data).json()
    #返回post请求结果
    return re





#查询门店-后台
def sysStore_search(sysStore,token):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/sysStore/search"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token
    }
    data={"pageNum": 1, "pageSize": 10, "keyword": sysStore,"needDataPermission":True,"chooseModel":True}

    re=requests.get(url=url,params=data,headers=headers).json()
    #返回post请求结果
    return re


#查询人员角色
def sysUser_loginInfo(userId,token):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-authorization/v1/sysUser/loginInfo"

    headers = {
        "Content-Type": "application/json",
        "token": token
    }
    data={"userId": userId}

    re=requests.get(url=url,params=data,headers=headers).json()
    #返回post请求结果
    return re

#查询请货商品
def goods_querySimple(token,departmentid,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/goods/querySimple"

    headers.update({
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    })

    re=requests.get(url=url,params=data,headers=headers).json()
    #返回post请求结果
    return re



#查询调拨，退货，报损，报溢商品
def goods_queryInvBatchNo(token,departmentid,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/goods/queryInvBatchNo"

    headers.update({
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    })

    re=requests.get(url=url,params=data,headers=headers).json()
    #返回post请求结果
    return re




#查询调拨，退货，报损，报溢商品批次信息
def goods_queryInvBatchInfo(token,departmentid,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/goods/queryInvBatchInfo"

    headers.update({
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    })

    re=requests.get(url=url,params=data,headers=headers).json()
    #返回post请求结果
    return re





#查询参林门店字典配置值-参林门店-239861260126519296，GSC自动补货-289980886798508032
def sysDictInfo_page(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/search/sysDictInfo/page"

    headers.update({
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    })

    re=requests.get(url=url,params=data,headers=headers).json()
    #返回post请求结果
    return re






#查询门店详情
def store_get(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/store/get"

    headers.update({
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    })

    re=requests.get(url=url,params=data,headers=headers).json()
    #返回post请求结果
    return re


#查询门店列表
def store_list(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/store/list"

    headers.update({
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    })

    re=requests.get(url=url,params=data,headers=headers).json()
    #返回post请求结果
    return re




def find_all_files(directory):
    """
    查找给定目录下的所有文件（包括子目录中的文件），并打印它们的完整路径。

    :param directory: 要搜索的目录路径
    :return: None，但会打印出所有文件的完整路径
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            # os.path.join用于将目录路径和文件名组合成完整路径
            full_path = os.path.join(root, file)
            print(full_path)

        # 示例用法


directory_to_search = "/path/to/your/directory"
find_all_files(directory_to_search)



if __name__ == '__main__':
    token =login()
    print("当前模块的名称是:", __name__)
    lists=read_csv("测试.csv")
    print(lists)
    list = []
    for i in lists:
        if i != []:
            if i[0] == "test_baosun":
                print(i)
                print(i[1:3])
                list.append(i[1:2])

    print(list)

