from heapq import  heapify, heappop, heappush
data = [1,3,5,7,9,2,4,6,8,0]
#rearrange the list into head order
heapify(data)
# add a new entry
heappush(data ,-5)
heappush(data , -10)
#fetch the three smallest entries
vv = [heappop(data) for i in range(3)]
print(vv)
