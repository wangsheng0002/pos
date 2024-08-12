import pytest

from function.function_baoyi import *
from function.function_tongyong import *
from function.function_LOG import *


lists=read_csv("测试.csv")
list=[]
for i in lists:
    if i[0]=="test_baoyi":
        list.append(i[1:3])

@pytest.mark.parametrize("sysStore,goodsNo", list)
def test_baoyi(sysStore, goodsNo):
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






    '''创建报溢总单'''
    # 创建报溢单总单,CHECK_OVERFLOW-盘点报溢
    data = {
        "departmentId": departmentid,
        "reasonDictCode": "CHECK_OVERFLOW"
    }
    req_order = inventoryOverflow_add(departmentid, token, data)
    logs('''创建报溢总单响应''', req_order)
    print('''创建报溢总单''', req_order)
    assert req_order.get("msg") == "保存成功", req_order.get("msg")
    # 提取总单单号
    overflowId = req_order.get("data")


    '''查询报溢单'''

    data = {
      "pageNum": 1,
      "pageSize": 60
    }
    re = inventoryOverflow_page(departmentid, token, data)
    logs('''查询报损总单响应''', req_order)

    for i in re.get("data").get("list"):
        if i.get("id")==overflowId:
            logs('''报损总单详情''', i)
            print('''报损总单详情''', i)
            break





    '''添加报溢商品'''
    # 查询请货商品
    data = {
        "pageNum": 1,
        "pageSize": 60,
        "goodsNo": goodsNo,
        "queryType": 3,
        "positionId": 0,
        "filterExpired": False,
        "queryThirtySaleQty": True,
        "largeClassType": 1
    }
    #查询报溢商品信息
    goods = goods_queryInvBatchNo(token, departmentid, data)

    print('''查询报溢商品信息''',goods)
    # 提取货品
    goods_lists = goods.get("data").get("list")
    if goods_lists==[]:
        print("找不到退货商品")
    #判断是否有数量
    for i in goods_lists:
        if i.get("inventory")>0:
            goods_list=i
            print('''报溢商品信息''',goods_list)
            break
        else:
            print("无可退数量")


    '''添加报溢商品'''
    data={
      "goodsName": goods_list.get("goodsName"),
      "goodsId": goods_list.get("goodsId"),
      "overflowId": overflowId,
      "producingBatchNo": goods_list.get("producingBatchNumber"),
      "num": 1,
      "positionId": "0",
      "positionName": "普通货位"
    }
    logs('''添加报溢商品入参''', data)
    print('''添加报溢商品入参''', data)
    req_add = inventoryOverflow_detail(departmentid, token, data)
    logs('''添加报溢商品响应''', req_add)
    print('''添加报溢商品''', req_add)
    assert req_add.get("msg") == "成功", req_add.get("msg")



    '''送审报溢单'''

    data = {
        "ids": overflowId,
        "checkState": 3
    }
    logs('''送审报溢商品入参''', data)
    re = inventoryOverflow_updateState(departmentid, token, data)
    logs('''送审报溢商品响应''', re)
    print('''送审报溢单''', re)
    assert re.get("msg") == "成功", re.get("msg")

    '''回退送审报溢单'''
    data = {
        "ids": overflowId,
        "checkState": 1
    }
    logs('''回退送审报溢商品入参''', data)
    re = inventoryOverflow_updateState(departmentid, token, data)
    logs('''回退送审报溢商品响应''', re)
    print('''回退送审报溢单''', re)
    assert re.get("msg") == "成功", re.get("msg")

    '''删除报溢单'''

    data = {
        "ids": overflowId
    }
    logs('''删除报溢商品入参''', data)
    re = inventoryOverflow(departmentid, token, data)
    logs('''删除报溢商品响应''', re)
    print('''删除报溢单''', re)
    assert re.get("msg") == "成功", re.get("msg")