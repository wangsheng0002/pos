import pytest

from function.function_qinghuo import *
from function.function_tongyong import *
from function.function_LOG import *

lists = read_csv("测试.csv")
list = []
for i in lists:
    if i[0] == "test_GSP":
        list.append(i[1:3])



#8101038 8101480
@pytest.mark.parametrize("sysStore,goodsNo", list)
# @pytest.mark.parametrize("sysStore,goodsNo", [("13628店",8112089)])

def test_qinghuo(sysStore,goodsNo):
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



    '''创建请货总单'''
    #创建请货单总单,2-订购
    data={
      "reqType": 2,
      "storeNo": storeNo,
      "storeName": storeName,
      "receiveUserName": username,
      "receiveUserNo": userno,
      "receiveUserPhone": phone,
      "receivingAddress": storeAddr,
      "singlePurchaseFlag": False,
      "positionId": 0,
      "tsfNo": ""
    }
    logs('''创建请货总单入参信息''', data)
    req_order = requestOrder_save(departmentid,token,data)
    print('''创建请货总单''',req_order)
    logs('''创建请货总单响应信息''', req_order)
    assert req_order.get("msg") == "成功", req_order.get("msg")
    #提取总单单号
    reqOrderId=req_order.get("data").get("reqOrderId")






    '''添加请货单商品'''
    #查询请货商品
    data={
        "pageNum": 1,
        "pageSize": 60,
        "goodsNo": goodsNo,
        "queryType": 1,
        "queryDepartmentId": departmentid,
        "filterExpired": False,
        "storeFilter": 1,
        "queryThirtySaleQty": True,
        "insuranceGoods": False
    }
    logs('''查询请货商品入参信息''', data)
    goods=goods_querySimple(token,departmentid,data)
    logs('''查询请货商品响应信息''', goods)
    print('''查询请货商品''',goods)
    #提取货品id
    goodsId=goods.get("data").get("list")[0].get("goodsId")
    #提取仓库库存
    warehouseInventory = goods.get("data").get("list")[0].get("warehouseInventory")

    #添加请货商品
    data={
      "reqOrderId": reqOrderId,
      "goodsId": goodsId,
      "reqGoodsQty": 1,
      "warehouseInventory": warehouseInventory
    }
    logs('''添加请货商品入参信息''', data)
    req_add=requestOrderDetail_modify(departmentid,token,data)
    print('''添加请货单商品''',req_add)
    logs('''添加请货商品响应信息''', req_add)
    assert req_add.get("msg") == "成功", req_add.get("msg")

    '''送审请货单'''
    data={
      "reqOrderIdList": [
          reqOrderId
      ],
      "submitType": 1
    }
    logs('''送审请货单入参信息''', data)
    re=requestOrder_submit(departmentid, token,data)
    logs('''送审请货单响应信息''', re)
    print('''送审请货单''',re)
    assert re.get("msg") == "成功", re.get("msg")


    '''回退送审请货单'''
    data={
      "reqOrderIdList": [
          reqOrderId
      ],
      "submitType": 0
    }
    logs('''回退送审请货单入参信息''', data)
    re=requestOrder_submit(departmentid, token,data)
    logs('''回退送审请货单响应信息''', re)
    print('''回退送审请货单''',re)
    assert re.get("msg") == "成功", re.get("msg")



    '''删除请货单'''
    data= [
      reqOrderId
    ]
    logs('''删除请货单入参信息''', data)
    re=requestOrder_del(departmentid, token,data)
    print('''删除请货单''',re)
    logs('''删除请货单响应信息''', re)

    assert re.get("msg") == "成功", re.get("msg")
