# Write a program which acceps % integer values and prints "Duplicates"
# if any of the values entered are duplicates otherwise it print " All Unique"
# Example Let 5 integers are 32,45,90,45,6 then output "Duplicates" to be printed

if __name__ == "__main__":
    l = list(map(int,input("Enter numbers separated by space: ").split()))
    s = set(l)
    if len(s) == len(l):
        print("All unique")
    else:
        print("Duplicates exist.\n No. of Duplicate elements = ", len(l) - len(s))
