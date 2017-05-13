import  bisect

scores  = [(100,'perl'),(200,'tcl'),(300,'lua')]
bisect.insort(scores,(400,'ruby'))
print(scores)