from datetime import datetime

import requests
import config.config_1


from function.function_tongyong import login

#查询补货单总单
def requestOrder_page(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-pos-management-provider/v1/requestOrder/page"

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
    print(datetime.now().strftime("%Y-%m-%d 00:00:00"))

    token =login().get("data").get("token")
    b = requestOrder_page("1",token,1)
    print(b)