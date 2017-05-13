try:
    raise  KeyboardInterrupt
finally:
    print("Goodbye world!")


# with  保证打开的文件被关闭
with open('myfile.txt') as f:
    for line in f:
        print(line)
