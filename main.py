import love2 as love_4
from love1 import love1 as love_1, love2 as love_2, love3 as love_3
if __name__ == '__main__':
    text = input('请输入心的类型:')
    love = 0
    try:
        love = int(text)
    except Exception as e:
        print("你输入的不是数字")

    if love == 1:
        love_1()
    elif love == 2:
        love_2()
    elif love == 3:
        love_3()
    elif love == 4:
        love_4()
