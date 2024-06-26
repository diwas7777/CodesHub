numRow=int(input('Enter the number of row: '))
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
    


# Output

#      *
#     * * 
#    * * * 
#   * * * * 
#  * * * * *



