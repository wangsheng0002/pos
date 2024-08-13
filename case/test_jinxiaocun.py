import pytest

from function.function_jinxiaocun import *
from function.function_tongyong import *
from function.function_LOG import *

lists = read_csv("测试.csv")
list = []
for i in lists:
    if i[0] == "test_jinxiaocun":
        list.append(i[1:3])

@pytest.mark.parametrize("sysStore,goodsNo", list)
def test_jinxiaocun(sysStore, goodsNo):
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



    '''查询门店出入库'''

    data={
    "pageNum": 1,
    "pageSize": 60,
    "businessStartTime": (datetime.now()-timedelta(days=7)).strftime("%Y-%m-%d 00:00:00"),
    "businessEndTime": datetime.now().strftime("%Y-%m-%d 23:59:59"),
    "departmentName": sysStore,
    "storeId": departmentid
    }
    re = goodsOutOfStockWarehousing_page(departmentid, token, data)
    logs( __name__+"---"+'''门店进销存信息''', re)
    print('''门店进销存信息''', re)
    assert re.get("msg") == "成功", re.get("msg")



    '''验证门店进销存是否有批次批号'''
    goodsBatch,producingBatchNumber=0,0
    for i in re.get("data").get("list"):
        if i.get("roleList") is not None:
            for j in i.get("roleList"):
                if j.get("goodsBatch") =='' and i.get("producingBatchNumber")== '':
                    goodsBatch=goodsBatch+1
                    producingBatchNumber=producingBatchNumber+1

                    print("存在批次批号空出入库记录"+i.get("documentNo"))
                    break
    assert goodsBatch<=1 or producingBatchNumber<=1 ,"存在批次批号空出入库记录"