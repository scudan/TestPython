import sys

try :
    f = open("myfile.txt")
    s = f.readline()#  有异常,且匹配则走异常分支,完了继续转到try.
    i = int(s.strip())
    print(i);
except IOError as err:
    print("I/O error:{0}".format(err))
except ValueError:
    print("Could not convert data to an integer!")
except:
    print("Unexpected error:",sys.exc_info()[0])
    raise