import  os,shutil
print(os.getcwd())
print(dir(os))

# copy 和 move file 和目录
shutil.copyfile('data.db','archive.db')
shutil.move('/build/executables','installdir')