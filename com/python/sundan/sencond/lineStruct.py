test = "hello" 'world'

print(test)
#[] 列表
#() 元组
#{} 字典

def fact(n):
    "this is function"
    if (n <= 1): return 1
    else: return n * fact(n-1)

print(fact.__doc__)
print(fact(5))