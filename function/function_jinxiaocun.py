from datetime import datetime,timedelta

import requests
import config.config_1


from function.function_tongyong import login

#查询进销存
def goodsOutOfStockWarehousing_page(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/goodsOutOfStockWarehousing/page"

    headers = {
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    }


    re=requests.get(url=url,params=data,headers=headers).json()

    #返回post请求结果
    return re












if __name__ == '__main__':
    token =login().get("data").get("token")
    print(token)
    b = goodsOutOfStockWarehousing_page("226831092781060177",token,{})
    print(b)