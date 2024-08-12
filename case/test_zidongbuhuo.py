import pytest

from function.function_zidongbuhuo import *
from function.function_tongyong import *
from function.function_LOG import *

lists = read_csv("测试.csv")
list = []
for i in lists:
    if i[0] == "test_zidongbuhuo":
        list.append(i[1:2])


#02048店广州龙溪西
@pytest.mark.parametrize("sysStore", list)
def test_zidongbuhuo(sysStore):
    '''#获取登录信息'''
    userlogin = login()
    print('''获取登录信息''',userlogin)
    logs("获取登录信息",userlogin)
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
    logs('''获取人员信息''', userinfo)
    #提取phone
    phone = userinfo.get("data").get("phone")



    '''获取门店信息'''
    Store =sysStore_search(sysStore,token)
    print('''获取门店信息''',Store)
    logs('''获取门店信息''', Store)
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
    logs('''查询参林门店字典''', re)
    "提取参林门店字典id"
    dictId=re.get("data").get("list")[0].get("dictId")
    '''查询参林门店字典是否配置门店'''
    data = {
        "pageNum": 1,
        "pageSize": 60,
        "dictCode": storeNo,
        "dictParentId": dictId
    }
    logs('''查询参林门店字典是否配置门店入参''', data)
    re=sysDictInfo_page(departmentid,token,data)
    logs('''查询参林门店字典是否配置门店响应''', re)
    print("参林门店配置",re)
    assert re.get("msg") == "成功" and re.get("data").get("total")== "1"



    '''查询门店类型，参林POS加盟店，直营店'''

    data={
        "pageNum": 1,
        "pageSize": 60,
        "storeName": sysStore
    }
    re_store=store_list(departmentid,token,data)
    logs('''查询门店类型''', re_store)
    print("门店信息",re_store)



    '''查询门店是否配置GSC自动补货'''
    data = {
        "pageNum": 1,
        "pageSize": 60,
        "dictTypeName": "GSC自动补货门店",
        "dictParentId": 0
    }

    re = sysDictInfo_page(departmentid, token, data)
    logs('''查询GSC自动补货字典''', re)

    "提取GSC自动补货门店字典id"
    dictId=re.get("data").get("list")[0].get("dictId")

    '''查询GSC自动补货门店字典是否配置门店'''
    data = {
        "pageNum": 1,
        "pageSize": 60,
        "dictCode": storeNo,
        "dictParentId": dictId
    }
    logs('''查询参林门店字典是否配置门店入参''', data)
    re=sysDictInfo_page(departmentid,token,data)
    logs('''查询参林门店字典是否配置门店响应''', re)
    print("GSC自动补货配置",re)
    #直营店需要配置GSC，加盟店不用配置
    if "加盟" not in re_store.get("data").get("list")[0].get("regionName"):
        assert re.get("msg") == "成功" and re.get("data").get("total")== "1"
    else:
        assert re.get("msg") == "成功" and re.get("data").get("total") == "0"



    '''查询门店自动补货单'''
    data = {
        "pageNum": 1,
        "pageSize": 60,
        "reqStartTime": datetime.now().strftime("%Y-%m-%d 00:00:00"),
        "reqEndTime": datetime.now().strftime("%Y-%m-%d 23:59:59"),
        "reqTypeList[0]": 7
    }
    re_order = requestOrder_page(departmentid, token, data)
    logs('''查询门店当天自动补货单响应''', re_order)
    print("门店自动补货单", re_order)
    assert re_order.get("msg") == "成功", re.get("msg")

    #直营店有自动补货单，加盟店无自动补货单
    if "加盟" not in re_store.get("data").get("list")[0].get("regionName"):

        # 判断当天自动补货单，每种类型数量小于等于1条
        x, y, z = 0, 0, 0
        for i in re_order.get("data").get("list"):

            if i.get("reqRemark") == "自动补货--成药":
                x = x + 1
            if i.get("reqRemark") == "自动补货--中药":
                y = y + 1
            if i.get("reqRemark") == "自动补货--参茸":
                z = z + 1

        assert x <= 1 and y <= 1 and z <= 1, "自动补货--成药:{}自动补货--中药:{}自动补货--参茸:{}".format(x, y, z)

    else:
        # 判断当天自动补货单，每种类型数量等于0条
        x, y, z = 0, 0, 0
        for i in re_order.get("data").get("list"):

            if i.get("reqRemark") == "自动补货--成药":
                x = x + 1
            if i.get("reqRemark") == "自动补货--中药":
                y = y + 1
            if i.get("reqRemark") == "自动补货--参茸":
                z = z + 1

        assert x == 0 and y == 0 and z == 0, "自动补货--成药:{}自动补货--中药:{}自动补货--参茸:{}".format(x, y, z)

