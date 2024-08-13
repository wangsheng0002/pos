import pytest

from function.function_GSP import *
from function.function_tongyong import *
from function.function_LOG import *

lists = read_csv("测试.csv")
list = []
for i in lists:
    if i[0] == "test_GSP":
        list.append(i[1:2])

@pytest.mark.parametrize("sysStore", list)
def test_GSP(sysStore):
    print("当前模块的名称是:", __name__)
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





    '''查询是门店角色是否存在对应角色'''

    '''查询门店人员'''

    data = {
        "pageNum": 1,
        "pageSize": 60,
        "departmentId": departmentid
    }
    re = sysUserRole_page(departmentid, token, data)
    logs( __name__+"---"+'''查询门店人员''', re)
    print('''门店人员信息''', re)
    assert re.get("msg") == "成功", re.get("msg")



    '''验证门店是否存在启用验收员'''
    userName=0
    for i in re.get("data").get("list"):
        if i.get("roleList") is not None:
            for j in i.get("roleList"):
                if "验收员" in j.get("roleName")and i.get("slUserStatus")==1:
                    logs( __name__+"---"+'''门店人员验收员角色''', i)
                    userName=userName+1
                    print("门店验收员"+i.get("userName"))
                    break
    assert userName>=1,"未找到启用验收员"