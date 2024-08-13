import pytest

from function.function_zidongbuhuo import *
from function.function_tongyong import *
from function.function_LOG import *

lists = read_csv("测试.csv")
list = []
for i in lists:
    if i[0] == "test_xitongpeizhi_GSC":
        list.append(i[1:2])

#02048店广州龙溪西
@pytest.mark.parametrize("sysStore", list)
def test_xitongpeizhi_GSC(sysStore):
    '''#获取登录信息'''
    userlogin = login()
    print('''获取登录信息''',userlogin)
    logs( __name__+"---"+"获取登录信息",userlogin)
    #提取token
    token = userlogin.get("data").get("token")
    #提取username
    username = userlogin.get("data").get("username")
    #提取userno
    userno = userlogin.get("data").get("empId")
    #提取userid
    userid = userlogin.get("data").get("id")


    '''获取人员信息'''
    userinfo = sysUser_loginInfo(userid,token)
    print('''获取人员信息''',userinfo)
    logs( __name__+"---"+'''获取人员信息''', userinfo)
    #提取phone
    phone = userinfo.get("data").get("phone")



    '''获取门店信息'''
    Store =sysStore_search(sysStore,token)
    print('''获取门店信息''',Store)
    logs( __name__+"---"+'''获取门店信息''', Store)
    #提取门店id
    departmentid=Store.get("data").get("list")[0].get("departmentId")
    #提取门店名称
    storeName=Store.get("data").get("list")[0].get("storeName")
    #提取门店名称
    storeNo=Store.get("data").get("list")[0].get("longStoreNo")
    #提取门店地址
    storeAddr=Store.get("data").get("list")[0].get("storeAddr")






    '''查询门店是否配置参林门店'''
    data = {
        "pageNum": 1,
        "pageSize": 60,
        "dictTypeName": "参林门店",
        "dictParentId": 0
    }
    re = sysDictInfo_page(departmentid, token, data)
    logs( __name__+"---"+'''查询参林门店字典''', re)
    "提取参林门店字典id"
    dictId=re.get("data").get("list")[0].get("dictId")
    '''查询参林门店字典是否配置门店'''
    data = {
        "pageNum": 1,
        "pageSize": 60,
        "dictCode": storeNo,
        "dictParentId": dictId
    }
    logs( __name__+"---"+'''查询参林门店字典是否配置门店入参''', data)
    re=sysDictInfo_page(departmentid,token,data)
    logs( __name__+"---"+'''查询参林门店字典是否配置门店响应''', re)
    print("参林门店配置",re)
    assert re.get("msg") == "成功" and re.get("data").get("total")== "1"



    '''查询门店是否配置订购无对接GSC批复'''
    data = {
        "pageNum": 1,
        "pageSize": 60,
        "dictTypeName": "订购无对接GSC批复",
        "dictParentId": 0
    }

    re = sysDictInfo_page(departmentid, token, data)
    logs( __name__+"---"+'''查询订购无对接GSC批复字典''', re)

    "提取订购无对接GSC批复门店字典id"
    dictId=re.get("data").get("list")[0].get("dictId")

    '''查询订购无对接GSC批复店字典是否配置门店'''
    data = {
        "pageNum": 1,
        "pageSize": 60,
        "dictCode": storeNo,
        "dictParentId": dictId
    }
    logs( __name__+"---"+'''查询参林门店字典是否配置订购无对接GSC批复''', data)
    re=sysDictInfo_page(departmentid,token,data)
    logs( __name__+"---"+'''查询参林门店字典是否配置订购无对接GSC批复响应''', re)
    print("GSC自动补货配置",re)
    assert re.get("msg") == "成功" and re.get("data").get("total") == "1"








