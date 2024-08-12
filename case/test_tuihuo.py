import pytest

from function.function_tuihuo import *
from function.function_tongyong import *


lists = read_csv("测试.csv")
list = []
for i in lists:
    if i[0] == "test_tuihuo":
        list.append(i[1:3])


@pytest.mark.parametrize("sysStore,goodsNo", list)
def test_tuihuo(sysStore, goodsNo):
    '''#获取登录信息'''
    userlogin = login()
    print('''#获取登录信息''', userlogin)
    # 提取token
    token = userlogin.get("data").get("token")
    # 提取username
    username = userlogin.get("data").get("username")
    # 提取userno
    userno = userlogin.get("data").get("empId")
    # 提取userid
    userid = userlogin.get("data").get("id")

    '''获取人员信息'''
    userinfo = sysUser_loginInfo(userid, token)
    print('''获取人员信息''', userinfo)
    # 提取phone
    phone = userinfo.get("data").get("phone")

    '''获取门店信息'''
    Store = sysStore_search(sysStore, token)
    print('''获取门店信息''', Store)
    # 提取门店id
    departmentid = Store.get("data").get("list")[0].get("departmentId")
    # 提取门店名称
    storeName = Store.get("data").get("list")[0].get("storeName")
    # 提取门店名称
    storeNo = Store.get("data").get("list")[0].get("longStoreNo")
    # 提取门店地址
    storeAddr = Store.get("data").get("list")[0].get("storeAddr")

    '''创建退货总单'''
    # 创建退货单总单,
    data = {
        "returnOrderType": "1",
        "reason": "5"
    }
    req_order = returnOrder_save(departmentid, token, data)
    print('''创建退货总单''', req_order)
    assert req_order.get("msg") == "成功", req_order.get("msg")
    # 提取总单单号
    returnOrderId = req_order.get("data").get("returnOrderId")

    '''添加退货单商品'''
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
    #查询退货商品信息
    goods = goods_queryInvBatchNo(token, departmentid, data)
    print(goods)
    # 提取货品
    goods_lists = goods.get("data").get("list")
    if goods_lists==[]:
        print("找不到退货商品")
    #判断是否有可退数量
    for i in goods_lists:
        if i.get("inventory")>0:
            goods_list=i
            print(goods_list)
            break
        else:
            print("无可退数量")




    # 添加退货商品
    # 设置退货数量，往商品里面添加退货数量字段
    return_goods = {
        "allotGoodsQty": 1,
        "detailRemark": "自动化测试",
        "returnGoodsQty": 1,
        "remarks": "自动化测试"

    }
    #退货商品信息更新
    goods_list.update(return_goods)


    '''退货商品校验'''
    data = {
        "returnOrder": {
            "returnOrderType": 1,
            "reason": "质量问题",
            "packageDamage": False,
            "returnOrderId": returnOrderId
        },
        "details": [
            goods_list
        ]
    }
    req_add = returnOrderDetail_check(departmentid, token, data)
    print('''检查退货商品''', req_add)
    assert req_add.get("checkResult") == True, req_add.get("msg")



    '''添加商品'''
    data = {
        "add": [
            goods_list
        ],
        "update": [],
        "del": [],
        "submitApprove": False,
        "returnOrder": {
            "returnOrderType": 1,
            "reason": "其他原因",
            "packageDamage": False,
            "returnOrderId": returnOrderId
        }
    }
    print(data)
    req_add = returnOrderDetail_modify(departmentid, token, data)
    print('''添加退货单商品''', req_add)
    assert req_add.get("msg") == "成功", req_add.get("msg")






    '''送审退货单'''
    data={
      "approveType": 1,
      "returnOrderIdList": [
        returnOrderId
      ]
    }
    re = returnOrder_sendApprove(departmentid, token, data)
    print('''送审请货单''', re)
    assert re.get("msg") == "成功", re.get("msg")

    '''回退送审退货单'''
    data={
      "approveType": 2,
      "returnOrderIdList": [
        returnOrderId
      ]
    }
    re = returnOrder_sendApprove(departmentid, token, data)
    print('''回退送审退货单''', re)
    assert re.get("msg") == "成功", re.get("msg")



    '''删除退货单'''

    data = {
        "returnOrderIdList": [
            returnOrderId
        ]
    }
    re = returnOrder_del(departmentid, token, data)
    print('''删除请货单''', re)
    assert re.get("msg") == "成功", re.get("msg")



    '''退货调拨'''

