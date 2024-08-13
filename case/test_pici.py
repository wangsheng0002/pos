import pytest

from function.function_pici import *
from function.function_tongyong import *
from function.function_LOG import *

lists = read_csv("测试.csv")
list = []
for i in lists:
    if i[0] == "test_pici":
        list.append(i[1:2])


#02048店广州龙溪西
@pytest.mark.parametrize("sysStore", list)
def test_pici(sysStore):
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








    '''查询门店类型，参林POS加盟店，直营店'''

    data={
        "pageNum": 1,
        "pageSize": 60,
        "storeName": sysStore
    }
    re_store=store_list(departmentid,token,data)
    logs( __name__+"---"+'''查询门店类型''', re_store)
    storeName=re_store.get("data").get("list")[0].get("storeName")
    areaName = re_store.get("data").get("list")[0].get("areaName")

    print("门店信息",re_store)


    #判断营运区是否开启多批次
    data = {
        "pageNum": 1,
        "pageSize": 100
    }
    re_Region=getRegionBatchConfigPage(departmentid,token,data)
    logs( __name__+"---"+'''查询开启营运区''', re_Region)
    re_Store = getStoreBatchConfigPage(departmentid, token, data)
    logs( __name__+"---"+'''查询开启门店''', re_Store)
    store=0
    for i in re_Region.get("data").get("list"):
        if areaName== i.get("regionName"):
            store=store+1
            print(i.get("regionName"),"已配置开启批次配置")
    for j in re_Store.get("data").get("list"):
        if storeName== j.get("storeName"):
            store=store+1
            print(j.get("storeName"), "已配置开启批次配置")


    assert store >=1









