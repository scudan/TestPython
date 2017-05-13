import  sys

for arg in sys.argv[1:]:
    try:
        f = open(arg,'r')
    except IOError:
        print('cannot open', arg)
        # 无异常,执行下面的语句,相当于finally
    else:
        print(arg,'has', len(f.readlines()),'lines')
        f.close()