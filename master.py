import random

name = input("输入软件名称：")
front = input("请输入激活码前缀，若无请不填：")

for j in range(1, 100):
    print("您的激活码为~~", front, end="")
    for i in range(1, 50):
        user = random.randint(33, 122)
        print(chr(user), end="")
    print(" ~~请复制波浪中的内容（不包括波浪和空格）使用此激活码激活/兑换", name)
