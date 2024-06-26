print ("*****TELEPHONE DIRECTORY***")
list1=[]
list2=[]
dict1={}
temp=100
n=int(input("Enter the number of contacts : "))
for i in range(0,n):
    name1=input("Enter your name: ")
    num=int(input("Enter your phone number: "))
    list1.extend([name1])
    list2.extend([num])
    dict1=dict(zip(list1,list2))#to convert two list into dictionary
print (dict1)

print ("""
         1:Add a contact
         2:Search a contact
         3:Delete a contact
         4:Update a contact
         5:View directory
         6:Exit""")
choice=input("Enter your choice")

def add(dict1):
    name3=raw_input("Enter the new name you want to add: ")
    num3=input("Enter the number: ")
    dict1[name3]=num3
    print (dict1)


def search(dict1,n,list1,temp):
    name2=raw_input("Enter the name whose number is to be found: ")
    for i in range(0,n):
        if list1[i]==name2:
            temp=i
    if temp!=100:
        print ("Number is : "),list2[temp]

def delete(dict1):
    name4=raw_input("Enter the name you want to delete: ")
    del dict1[name4]
    print (dict1)

def update(dict1,n,list1):
    name5=raw_input("Enter the name which you want to update: ")
    for i in range(0,n):
        if list1[i]==name5:
            temp=i
    if temp!=100:
        num5=input("Enter the new number")
        dict1[name5]=num5
    print (dict1)
def view(dict1):
    print (dict1)

if (choice==1):
    add(dict1)
elif (choice==2):
   search(dict1,n,list1,temp)
elif (choice==3):
    delete(dict1)
elif (choice==4):
    update(dict1,n,list1)
else:
    view(dict1)