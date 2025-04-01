def area(length: int,breadth: int):
    """
    Function to find area of rectangle
    """
    return length*breadth

if __name__ == "__main__":
    l = int(input("enter the length of rectangle : "))
    b = int(input("enter the breadth of the rectangle : "))
    print(area(l,b))