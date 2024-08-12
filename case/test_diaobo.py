from time import sleep

import pytest

from function.function_diaobo import *
from function.function_tongyong import *
from function.function_shouhuo import *
from function.function_LOG import *

lists = read_csv("测试.csv")
list = []
for i in lists:
    if i[0] == "test_diaobo":
        list.append(i[1:4])


#8901005   8201947
# @pytest.mark.parametrize("sysStore,goodsNo,sysStore2,", read_csv("测试.csv")[1:])
@pytest.mark.parametrize("sysStore,goodsNo,sysStore2,", list)
def test_diaobo(sysStore, goodsNo,sysStore2):
    '''#获取登录信息'''
    userlogin = login()
    print('''获取登录信息''', userlogin)
    logs("#获取登录信息", userlogin)
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
    logs("获取人员信息", userinfo)
    print('''获取人员信息''', userinfo)
    # 提取phone
    phone = userinfo.get("data").get("phone")

    '''获取调出门店信息'''
    Store = sysStore_search(sysStore, token)
    logs("获取调出门店信息", Store)
    print('''获取调出门店信息''', Store)
    # 提取门店id
    departmentid = Store.get("data").get("list")[0].get("departmentId")
    # 提取门店名称
    storeName = Store.get("data").get("list")[0].get("storeName")
    # 提取门店名称
    storeNo = Store.get("data").get("list")[0].get("longStoreNo")
    # 提取门店地址
    storeAddr = Store.get("data").get("list")[0].get("storeAddr")

    '''获取接收门店信息'''
    Store2 = sysStore_search(sysStore2, token)
    logs("获取接收门店信息", Store2)
    print('''获取接收门店信息''', Store2)
    # 提取门店id
    departmentid2 = Store2.get("data").get("list")[0].get("departmentId")
    # 提取门店名称
    storeName2 = Store2.get("data").get("list")[0].get("storeName")
    # 提取门店名称
    storeNo2 = Store2.get("data").get("list")[0].get("longStoreNo")
    # 提取门店地址
    storeAddr2 = Store2.get("data").get("list")[0].get("storeAddr")




    '''创建调拨总单'''
    # 创建调拨总单,
    data = {
    }
    req_order = allotOrder_save(departmentid,token,data)
    logs("创建调拨总单响应", req_order)
    print('''创建调拨总单''', req_order)
    assert req_order.get("msg") == "成功", req_order.get("msg")
    # 提取总单单号
    allotOrderId = req_order.get("data").get("allotOrderId")
    allotOrderNo = req_order.get("data").get("allotOrderNo")

    '''添加调拨细单商品'''
    # 查询调拨商品
    data = {
        "pageNum": 1,
        "pageSize": 60,
        "goodsNo": goodsNo,
        "queryType": 3,
        "positionId": 0,
        "filterExpired": False,
        "queryThirtySaleQty": True
    }
    logs("查询调拨商品入参", data)
    #查询调拨商品信息
    goods = goods_queryInvBatchNo(token, departmentid, data)
    logs("查询调拨商品响应", goods)
    print("查询调拨商品",goods)
    # 提取货品
    goods_lists = goods.get("data").get("list")
    if goods_lists==[]:
        print("找不到退货商品")
    #判断是否有可调拨数量
    for i in goods_lists:
        if i.get("inventory")>0:
            # 保留批号，用于反向调回
            producingBatchNumber = i.get("producingBatchNumber")
            producingBatchNumberId = i.get("producingBatchNumberId")
            goodsId = i.get("goodsId")
            goods_list=i
            print("选择调拨商品",goods_list)
            break

    #添加批次
    data = {
        "departmentId": departmentid,
        "inventoryFilter": True,
        "producingBatchNumberId": producingBatchNumberId,
        "positionId": 0
    }
    logs("添加批次入参", data)
    # 查询调拨商品信息
    queryInvBatchInfo = goods_queryInvBatchInfo(token, departmentid, data)
    logs("添加批次响应", queryInvBatchInfo)
    print("批次信息",queryInvBatchInfo)
    #更新批号信息
    goods_list.update(queryInvBatchInfo.get("data")[0])

    # 添加调拨商品
    # 设置调拨数量，往商品里面添加调拨数量字段
    allot_goods = {
        "allotGoodsQty": 1,
        "allotDetailStatus": 1,
        "allotPrice": None,
        "allotDetailAmount": None

    }
    #调拨商品信息更新
    goods_list.update(allot_goods)
    data = {
        "add": [
            goods_list
        ],
        "update": [],
        "del": [],
        "submitApprove": False,
        "allotOrderId": allotOrderId,
        "allotType": 1,
        "allotObjId": departmentid2
    }

    logs("添加调拨单商品入参", data)
    req_add = allotOrderDetail_modify(departmentid, token, data)
    logs("添加调拨单商品响应", req_add)
    print('''添加调拨单商品''', req_add)
    assert req_add.get("msg") == "成功", req_add.get("msg")



    '''校验商品是否允许调拨'''

    data = {
      "producingBatchNumber": producingBatchNumber,
      "allotObjId": allotOrderId,
      "goodsId": goodsId,
      "departmentId": departmentid
    }
    logs("校验商品是否允许调拨入参", data)
    print('调拨信息检查',data)
    re = allotOrderDetail_check(departmentid, token, data)
    logs("校验商品是否允许调拨响应", re)
    print('''校验商品是否允许调拨''', re)
    assert re.get("msg") == "成功", re.get("msg")




    '''送审调拨单'''

    data = {
        "allotOrderId": allotOrderId
    }
    logs("送审调拨单入参", data)
    re = allotOrder_submit(departmentid, token, data)
    print('''送审请调拨''', re)
    logs("送审调拨单响应", re)
    assert re.get("msg") == "成功", re.get("msg")

    sleep(3)
    '''接收门店收货'''
    #查询收货单
    data = {"pageNum": 1, "pageSize": 20, }
    re = acceptOrder_page(departmentid2, token, data)
    logs("接收门店查询收货单", re)
    #找到调拨单号
    for i in re.get("data").get("list"):
        if i.get("tsfNo")==allotOrderNo:
            logs("收货单", i)
            print("收货单", i)
            distributeOrderId=i.get("distributeOrderId")
            break


    #整单收货
    data={
      "id": distributeOrderId
    }
    logs("整单收货入参", data)
    re_acc=acceptOrder_accept(departmentid2, token, data)
    logs("整单收货响应", re_acc)
    print('''整单收货''', re_acc)
    assert re_acc.get("msg") == "成功", re_acc.get("msg")




    '''调回调出门店'''
    '''创建调拨总单'''
    # 创建调拨总单,
    data = {
    }
    req_order = allotOrder_save(departmentid2,token,data)
    logs("调回调出门店-创建调拨总单响应", req_order)
    print('''调回调出门店-创建调拨总单''', req_order)
    # 提取总单单号
    allotOrderId = req_order.get("data").get("allotOrderId")
    allotOrderNo = req_order.get("data").get("allotOrderNo")

    '''添加调拨细单商品'''
    # 查询调拨商品
    data = {
        "pageNum": 1,
        "pageSize": 60,
        "goodsNo": goodsNo,
        "queryType": 3,
        "positionId": 0,
        "filterExpired": False,
        "queryThirtySaleQty": True,
    }
    #查询调拨商品信息
    goods = goods_queryInvBatchNo(token, departmentid2, data)
    logs("调回调出门店-查询调拨商品", goods)
    print("调回调出门店-查询调拨商品",goods)
    # 提取货品
    goods_lists = goods.get("data").get("list")
    if goods_lists==[]:
        print("调回调出门店-找不到退货商品")
    #判断是否有可调拨数量
    for i in goods_lists:
        #找到刚收货商品的批号
        if i.get("producingBatchNumber")==producingBatchNumber:
            producingBatchNumberId2=i.get("producingBatchNumberId")
            goods_list=i
            print("调回调出门店-选择调拨商品",goods_list)
            break


    #添加批次
    data = {
        "departmentId": departmentid2,
        "inventoryFilter": True,
        "producingBatchNumberId": producingBatchNumberId2,
        "positionId": 0
    }
    logs("调回调出门店-添加批次入参", data)
    # 查询调拨商品信息
    queryInvBatchInfo = goods_queryInvBatchInfo(token, departmentid2, data)
    logs("调回调出门店-添加批次响应", data)
    #更新批号信息
    goods_list.update(queryInvBatchInfo.get("data")[0])

    # 添加调拨商品
    # 设置调拨数量，往商品里面添加调拨数量字段
    allot_goods = {
        "allotGoodsQty": 1,
        "allotDetailStatus": 1,
        "allotPrice": None,
        "allotDetailAmount": None

    }
    #调拨商品信息更新
    goods_list.update(allot_goods)
    data = {
        "add": [
            goods_list
        ],
        "update": [],
        "del": [],
        "submitApprove": False,
        "allotOrderId": allotOrderId,
        "allotType": 1,
        "allotObjId": departmentid
    }
    logs("调回调出门店-添加调拨单商品入参", data)
    req_add = allotOrderDetail_modify(departmentid2, token, data)
    logs("调回调出门店-添加调拨单商品响应", data)
    print('''调回调出门店-添加调拨单商品''', req_add)



    '''校验商品是否允许调拨'''

    data = {
        "producingBatchNumber": producingBatchNumber,
        "allotObjId": allotOrderId,
        "goodsId": goodsId,
        "departmentId": departmentid2
    }
    logs("调回调出门店-校验商品是否允许调拨入参", data)
    re = allotOrderDetail_check(departmentid, token, data)
    logs("调回调出门店-校验商品是否允许调拨响应", re)
    print('''调回调出门店-校验商品是否允许调拨''', re)
    assert re.get("msg")=="成功",re.get("msg")







    '''送审调拨单'''

    data = {
        "allotOrderId": allotOrderId
    }
    logs("调回调出门店-送审调拨单入参", data)
    re = allotOrder_submit(departmentid2, token, data)
    logs("调回调出门店-送审调拨单响应", re)
    print('''调回调出门店-送审请调拨''', re)

    sleep(3)

    '''调出门店收货'''
    #查询收货单
    data = {"pageNum": 1, "pageSize": 20, }
    re = acceptOrder_page(departmentid, token, data)
    logs("调回调出门店-询收货单", re)
    #找到调拨单号
    for i in re.get("data").get("list"):
        if i.get("tsfNo")==allotOrderNo:
            logs("收货单", i)
            print("收货单", i)
            distributeOrderId=i.get("distributeOrderId")
            break

    #整单收货
    data={
      "id": distributeOrderId
    }
    logs("调回调出门店-整单收货入参", data)
    re_acc=acceptOrder_accept(departmentid, token, data)
    logs("调回调出门店-整单收货响应", re_acc)
    print('''调回调出门店-整单收货''', re_acc)