def revstring(string):
    if len(string) == 0:
        return(string)
    else:
        return revstring(string[1:])+string[0]
        
stg = input("Enter a string: ")
print("The reversed string is: ", end=" ") 
print(revstring(stg))