# PROBLEM STATEMENT:
# Given to you shall be a number, within the range from 0 to 9. Draw a set of triangles which sit inside each other.
# The number of triangles is equal to the input received. Please not that in the example a 0 input implies a 0 triangle.
#  
# INPUT:
# The input shall be a single integer from 0 to 9.
#
# OUTPUT:
# The output should be the pattern of triangles inside triangles.
#
# EXAMPLE:
# Input:
# 1
# 
# Output:
#  1 
# 111
# 
# Input:
# 0
# 
# Output:
# 0
# 
# Input:
# 2
# 
# Output:
#    2
#   212
#  21112
# 2222222


def triangleloop(num):
  rows = []
  if(num == 0):
    rows =["0"]
  elif(num == 1):
    rows = ["1", "111"]
  else:
    listTmp = triangleloop(num-1)
    rows = [num]
    for i in listTmp:
      rows.append(str(num) + str(i) + str(num))
    rows.append(str(num)* (len(rows[-1])+2))
  return rows

n = input()
l = triangleloop(int(n))
if(len(l) != 0):
  size = len(l[-1])
  steps = int(size/2)
  for i in l:
    res = ((str(" ") * steps) + str(i))
    steps= steps - 1
    print(res)