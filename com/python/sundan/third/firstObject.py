items = { # 定义一个字典
    'number' : 43,
    'text': "Hw"
}

# 字典添加值

#添加函数
items['func'] = abs
import  math
#添加模块
items['mod'] = math
#添加对象
items['error'] = ValueError

nums = [1,3,5]
#添加对象的一个方法
items['append'] = nums.append
items['append'](-45)
print(items['mod'].sqrt(4) )