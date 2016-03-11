#生成器:结果生成一个序列,而不仅仅是一个值

def countdown(n):
    print("Count down!");
    while n > 0:
        yield (n)
        n -= 1;

for i in countdown(10):
 print(i);

