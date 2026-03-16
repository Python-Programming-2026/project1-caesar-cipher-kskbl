def caesar_cipher(text, move, a=1):   #定义凯撒密码函数，text为输入文本，move为位移量，a=1和a=-1分别表示加密和解密
    result = ""    #设置空字符串用于存放转化后的文本
    if a == -1:
       move = -move     #若为解密则朝逆方向移动
    for single in text:     #对逐个字母进行处理
        if single.isupper():
            moved_single = chr((ord(single)-65+move)%26+65)     #对大写字母进行处理
            result = result+moved_single                #处理完插入result中
        elif single.islower():
            moved_single = chr((ord(single)-97+move)%26+97)     #对小写字母进行处理
            result = result+moved_single                #处理完插入result中
        else:
            result = result+single             #遇到空格则不做处理
    return result
if __name__ == "__main__":
    print("凯撒密码")
    usertext=input("请输入文本:")  #获取输入的待处理文本
    while True:
       usermove=int(input("请输入位移量："))     # 将输入的位移量转为整数
       if usermove>=0:           # 判断位移量是否为非负整数
            break   #输入合法
       else:        #输入不合法
           print("位移量是非负整数")   #报错
    while True:
        usermode=input("请选择加密：1或解密：-1:")   # 获取用户输入的模式
        if usermode in ["1", "-1"]:     # 判断输入是否为合法选项
            user_mode = int(usermode)   # 将模式字符串转为整数
            break
        else:
            print("请输入1或-1")
result = caesar_cipher(usertext, usermove, user_mode)# 调用凯撒密码函数，传入用户输入的文本、位移量和模式
print(f"\n{result}")     # 打印最终处理结果
