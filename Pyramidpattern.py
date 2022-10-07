numRow=int(input('ENter the number of row\n'))
sp=numRow-1
st=1
for i in range(numRow):
    for j in  range(sp):
        print(end=' ')
    for j in range(st):
        print('*',end=' ')
    print()
    sp-=1
    st+=1
    
/*

    *
   * * 
  * * * 
 * * * * 
* * * * *


*/
