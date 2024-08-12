import csv
import time

import requests
import config.config_1
from function.function_tongyong import login



#查询角色

def sysUser_query(userId,token):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-authorization/v1/sysUser/query"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token
    }
    data={"userId": userId}
    re=requests.get(url=url,params=data,headers=headers).json()
    #返回post请求结果
    return re

#查询门店
def sysStore_page(search,token):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-retail-provider/v1/sysStore/page"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token
    }
    data={"pageNum": 1, "pageSize": 10, "search": search}
    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re

#查询班次
def checkClassesSetting(departmentid,token):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-retail-provider/v1/classesSetting/checkClassesSetting"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }
    re=requests.get(url=url,headers=headers).json()
    #返回post请求结果
    return re

#选择班次
def recordClasses(departmentid,token,accountingDay,classesSettingId):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-retail-provider/v1/classesSetting/recordClasses"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }
    data = {"accountingDay": accountingDay, "classesSettingId": classesSettingId}
    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re


#查询商品
def goods_page(departmentid,token,search):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-retail-provider/v1/goods/page"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }
    data = {"pageNum": 1, "pageSize": 10, "search": search}
    re=requests.get(url=url,params=data,headers=headers).json()
    #返回post请求结果
    return re


#查询营业员
def sysUser_page(departmentid,token):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-retail-provider/v1/sysUser/page"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }
    data = {"pageNum": 1, "pageSize": 10, "departmentId": departmentid}
    re=requests.get(url=url,params=data,headers=headers).json()
    #返回post请求结果
    return re


#添加商品
def shoppingCart_add(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-retail-provider/v1/shoppingCart/add"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re




#结算pageup
def order_page_up(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-retail-provider/v1/order/page_up"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }

    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re




#支付完成
def pay_cash_pay(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-retail-provider/pay/cash_pay"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }
    data={"orderSalesId": "367171427649974272", "payAmount": 23.85, "usePoints": 0, "couponInfoList": [], "financeCenterId": 1, "isManualPayment": False}
    re=requests.post(url=url,json=data,headers=headers).json()
    #返回post请求结果
    return re



if __name__ == '__main__':
    a={"ts": 1718274245769, "accountingDay": "2024-06-13", "memberCouponExecuteDtoList": [], "member": {"register": False, "memberType": 1}, "operation": {"operationType": 1}, "shoppingCartDetailReqList": [{"promotionDetailList": [], "_id": "273239565775192064", "goodsId": "179096350883864579", "goodsNo": "8101480", "goodsName": "夏桑菊颗粒(星群)", "producingArea": "广州", "specifications": "10g*28袋", "pushClass": "B", "price": 26.5, "memberPrice": 26, "ephedrine": False, "specialMedicines": False, "rxOtcType": 4, "manageStatus": 0, "gscGoodsStatus": "A", "deptCode": None, "goodsType": 0, "groupsId": "177149332036149248", "deptId": "177149381537325057", "isTcm": 0, "nearTermDays": 30, "packageNum": None, "groupsCode": "11", "units": None, "incaGoodsId": "103", "goodsElectronicSupervisionCodePackageType": None, "isInputElectronicSupervisionCode": 0, "goodsInTax": None, "goodsOutTax": None, "isInsuranceGoods": 1, "producingBatchNumber": "SC90215", "producingBatchNumberId": "273239565775192064", "availableInventory": 99918, "producingDate": "2021-09-09 00:00:00.000", "expiryDate": "2024-08-31 00:00:00.000", "expiry": False, "updateTime": "2024-06-08 01:52:43.101", "_pid": "5", "goodsNum": 1, "_class_name": "", "_disabled": False, "highRisk": False, "mixType": None, "salesmanId": "226834434664075501", "salesmanName": "肖敏", "detailType": 0}]}
    c={"accountingDay": "2024-06-13", "classesSettingId": "297488679720251392", "classesName": "A", "member": {}, "goodsList": [{"isJoinExpiration": False, "frontId": None, "chineseMedicineOrder": None, "groupOrder": None, "detailId": "367167080891412480", "parentDetailId": None, "goodsId": "179096350883864579", "dismantleId": None, "goodsNo": "8101480", "goodsName": "夏桑菊颗粒(星群)", "availableInventory": 99918, "pushClass": "B", "memberRate": None, "price": 26.5, "memberPrice": 26, "dismantlePrice": None, "exchangeMoney": None, "unitTradePrice": None, "usePrice": 23.85, "realPrice": 23.85, "goodsNum": 1, "producingBatchNumberId": "273239565775192064", "producingBatchNumber": "SC90215", "specifications": "10g*28袋", "salesmanId": "226834434664075501", "salesmanName": "肖敏", "ephedrine": False, "miClassText": "医保", "isTcm": False, "highRisk": False, "mixType": None, "goodsType": 0, "factoryName": "广州白云山明兴制药有限公司", "producingArea": "广州", "expiryDays": 80, "expiryDate": "2024-08-31 00:00:00.000", "approveNo": "国药准字Z44022217", "medicalInsuranceCoding": "ZA04BAX0061020300423", "rxOtcType": 4, "memberDiscountFlag": False, "nearlyPrice": None, "nearlyFlag": False, "limitFlag": "", "limitDesc": None, "comboLimitFlag": None, "detailType": 0, "actualReceivableMoney": 23.85, "receivableMoney": 26.5, "pointExchangeGoods": None, "usePoint": None, "prescriptionGoods": None, "prescriptionId": None, "activityId": 4825, "ruleId": 26584, "ruleType": 5, "eventId": 182129, "rewardId": None, "themeId": 117, "groupId": None, "ruleEventTypeDesc": "主推折扣", "ruleEventList": [{"detailId": "367167080891412480", "activityId": 4825, "ruleId": 26584, "ruleType": 5, "eventId": 182129, "ruleEventTypeDesc": "主推折扣", "ruleEventTypeSimpleDesc": "折扣", "promotionDesc": "满11元起9折", "executeFlag": True}], "noExecSingleProm": False, "noExecWholeProm": False, "couponOverlyingFlag": "0", "useCoupon": False, "manualDiscountFlag": None, "wholeLevelAmount": None, "exchangeGroupNum": None, "comboUniqueId": None, "comboGoodsId": None, "comboGoodsName": None, "comboGoodsNum": None, "comboPrice": None, "promotionDetailList": [{"detailId": "367167080891412480", "activityId": 4825, "ruleId": 26584, "ruleType": 5, "eventId": 182129, "ruleEventTypeDesc": "主推折扣", "promotionDesc": "满11元起9折", "executeFlag": True}], "giftList": None, "exchangeGoodsList": None, "coupons": None, "giftCardList": None, "canDiscount": True, "voucherAllocatedMoney": None, "specialMedicines": False, "groupsCode": "11", "feeType": None, "isInputElectronicSupervisionCode": 0, "electronicSupervisionCodes": None, "children": [], "_X_ROW_CHILD": [], "promotion": {"frontId": None, "chineseMedicineOrder": None, "groupOrder": None, "detailId": "367167080891412480", "parentDetailId": None, "goodsId": "179096350883864579", "dismantleId": None, "goodsNo": "8101480", "goodsName": "夏桑菊颗粒(星群)", "availableInventory": 99918, "pushClass": "B", "memberRate": None, "price": 26.5, "memberPrice": 26, "dismantlePrice": None, "exchangeMoney": None, "unitTradePrice": None, "usePrice": 23.85, "realPrice": 23.85, "goodsNum": 1, "producingBatchNumberId": "273239565775192064", "producingBatchNumber": "SC90215", "specifications": "10g*28袋", "salesmanId": "226834434664075501", "salesmanName": "肖敏", "ephedrine": False, "miClassText": "医保", "isTcm": False, "highRisk": False, "mixType": None, "goodsType": 0, "factoryName": "广州白云山明兴制药有限公司", "producingArea": "广州", "expiryDays": 80, "expiryDate": "2024-08-31 00:00:00.000", "approveNo": "国药准字Z44022217", "medicalInsuranceCoding": "ZA04BAX0061020300423", "rxOtcType": 4, "memberDiscountFlag": False, "nearlyPrice": None, "nearlyFlag": False, "limitFlag": "", "limitDesc": None, "comboLimitFlag": None, "detailType": 0, "actualReceivableMoney": 23.85, "receivableMoney": 26.5, "pointExchangeGoods": None, "usePoint": None, "prescriptionGoods": None, "prescriptionId": None, "activityId": 4825, "ruleId": 26584, "ruleType": 5, "eventId": 182129, "rewardId": None, "themeId": 117, "groupId": None, "ruleEventTypeDesc": "主推折扣", "ruleEventList": [{"detailId": "367167080891412480", "activityId": 4825, "ruleId": 26584, "ruleType": 5, "eventId": 182129, "ruleEventTypeDesc": "主推折扣", "ruleEventTypeSimpleDesc": "折扣", "promotionDesc": "满11元起9折", "executeFlag": True}], "noExecSingleProm": False, "noExecWholeProm": False, "couponOverlyingFlag": "0", "useCoupon": False, "manualDiscountFlag": None, "wholeLevelAmount": None, "exchangeGroupNum": None, "comboUniqueId": None, "comboGoodsId": None, "comboGoodsName": None, "comboGoodsNum": None, "comboPrice": None, "promotionDetailList": [{"detailId": "367167080891412480", "activityId": 4825, "ruleId": 26584, "ruleType": 5, "eventId": 182129, "ruleEventTypeDesc": "主推折扣", "promotionDesc": "满11元起9折", "executeFlag": True}], "giftList": None, "exchangeGoodsList": None, "manualDiscount": None, "coupons": None, "giftCardList": None, "canDiscount": True, "voucherAllocatedMoney": None, "specialMedicines": False, "groupsCode": "11", "feeType": None, "isInputElectronicSupervisionCode": 0, "electronicSupervisionCodes": None, "children": [], "_X_ROW_CHILD": []}, "promotions": [{"comboUniqueId": None, "comboGoodsId": None, "comboGoodsName": None, "comboGoodsNum": None, "comboPrice": None, "detailId": "367167080891412480", "activityId": 4825, "ruleId": 26584, "ruleType": 5, "eventId": 182129, "ruleEventTypeDesc": "主推折扣", "promotionDesc": "满11元起9折", "executeFlag": True}]}]}
    b=order_page_up("226831092781060177",c)
    print(b)