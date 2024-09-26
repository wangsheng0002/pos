import requests
import config.config_1


from function.function_tongyong import login
headers=config.config_1.headers_pro
#查询角色
def sysUserRole_page(departmentid,token,data):
    #引用配置的域名
    url = config.config_1.url_pro+"/api/sl-authorization/v1/sysUserRole/page"

    headers.update({
        "Content-Type": "application/json",
        "sl-mode":"store",
        "token": token,
        "sl-mode-department-id":departmentid
    })


    re=requests.get(url=url,params=data,headers=headers).json()

    #返回post请求结果
    return re












if __name__ == '__main__':
    token =login().get("data").get("token")
    print(token)
    b = sysUserRole_page("226831092781060177",token,{})
    print(b)