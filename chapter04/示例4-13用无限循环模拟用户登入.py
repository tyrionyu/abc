i=0
while i<3:
    user_name=input('请输入用户名：')
    pwd=input('请输入密码：')
    if user_name=='admin' and pwd=='6666':
        print('系统正在登录，请稍后')
        i=10
    else:
        if i<2:
            print('用户名或密码不正确,您还有',2-i,'次机会')
        i+=1
if i==3:
    print('对不起，密码输入三次错误！')
