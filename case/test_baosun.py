import pytest

from function.function_baosun import *
from function.function_tongyong import *
from function.function_LOG import *

lists=read_csv("测试.csv")
list=[]
for i in lists:
    if i[0]=="test_baosun":
        list.append(i[1:3])



@pytest.mark.parametrize("sysStore,goodsNo", list)
def test_baosun(sysStore, goodsNo):
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



    '''创建报损总单'''
    # 创建报溢单总单,订单枚举1成药2中药3参茸4物质赠品
    data = {
      "groupType": "1",
      "remarks": "自动化测试验证"
    }
    req_order = lossReportingOrder_saveOrUpdate(departmentid, token, data)
    logs( __name__+"---"+'''创建报损总单响应''', req_order)
    print('''创建报损总单''', req_order)
    assert req_order.get("msg") == "成功", req_order.get("msg")
    # 提取总单单号
    LossReportingOrderId = req_order.get("data")




    '''查询报损单'''

    data = {
      "pageNum": 1,
      "pageSize": 60
    }
    re = lossReportingOrder_page(departmentid, token, data)
    logs( __name__+"---"+'''查询报损总单响应''', req_order)

    for i in re.get("data").get("list"):
        if i.get("id")==LossReportingOrderId:
            logs( __name__+"---"+'''报损总单详情''', i)
            print('''报损总单详情''', i)
            break



    '''添加报损商品'''
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
    logs( __name__+"---"+'''查询报损商品信息''', goods)
    print('''查询报损商品信息''',goods)
    # 提取货品
    goods_lists = goods.get("data").get("list")
    if goods_lists==[]:
        print("找不到报损商品")
    #判断是否有数量
    for i in goods_lists:
        if i.get("inventory")>0:
            goods_list=i
            print("报损商品信息",goods_list)
            break
        else:
            print("无可报损数量")


    '''添加报损商品'''

    #报损枚举盘亏102，商品破损333，质量问题322等

    data = {
        "lossReportingGoodsQty": 1,
        "reasonDictCode": "102",
        "specificReasonDictCode": "1",
        "goodsId": goods_list.get("goodsId"),
        "goodsName": goods_list.get("goodsName"),
        "goodsNo": goods_list.get("goodsNo"),
        "producingBatchNumber": goods_list.get("producingBatchNumber"),
        "producingBatchNumberId": goods_list.get("producingBatchNumberId"),
        "goodsLossReportingOrderId": LossReportingOrderId,
        "positionId": "0",
        "positionName": "普通货位",
        "rtClassText": goods_list.get("rtClassText"),
        "validDate": goods_list.get("validDate")
    }
    logs( __name__+"---"+'''添加报损商品入参''', data)
    print('''添加报损商品入参''', data)
    req_add = lossReportingOrder_detailSaveOrUpdate(departmentid, token, data)
    logs( __name__+"---"+'''添加报损商品响应''', req_add)
    print('''添加报损商品''', req_add)
    assert req_add.get("msg") == "成功", req_add.get("msg")



    '''送审报损单'''

    data = {
        "lossReportingOrderId": [
            LossReportingOrderId
        ],
        "approveStatus": 3
    }
    logs( __name__+"---"+'''送审报损单入参''', data)
    re = lossReportingOrder_approve(departmentid, token, data)
    logs( __name__+"---"+'''送审报损单响应''', re)
    print('''送审报损单''', re)
    assert re.get("msg") == "成功", re.get("msg")

    '''回退送审报损单'''
    data = {
        "lossReportingOrderId": [
            LossReportingOrderId
        ],
        "approveStatus": 1
    }
    logs( __name__+"---"+'''回退报损单入参''', data)
    re = lossReportingOrder_approve(departmentid, token, data)
    logs( __name__+"---"+'''回退报损单响应''', re)
    print('''回退送审报损单''', re)
    assert re.get("msg") == "成功", re.get("msg")

    '''删除报损单'''

    data = [
        LossReportingOrderId
    ]
    logs( __name__+"---"+'''删除报损单入参''', data)
    re = lossReportingOrder_delete(departmentid, token, data)
    logs( __name__+"---"+'''删除报损单响应''', re)
    print('''删除报损单''', re)
    assert re.get("msg") == "成功", re.get("msg")