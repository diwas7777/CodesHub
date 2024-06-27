import math


def Area(s1: float, s2: float, s3: float):
    """
    Function to find area of triangle

    params:
        s1: float: an int type value
        s2: float: an int type value
        s3: float: an int type value

    return:
        area: float: Calculated area of three sided triangle.
    """
    area = 0
    if(s1 == s2 == s3):
        area = (math.sqrt(3)/4) * math.pow(s1,2)
    elif(s1 == s2 or s2 == s3 or s1 == s3):
        if(s1 == s2):
            area = 0.5 * s1 * s3
        elif(s2 == s3):
            area = 0.5 * s2 * s1
        elif(s1 == s3):
            area = 0.5 * s3 * s2
    else:
        sp = (s1 + s2 + s3) / 2
        area = math.sqrt(sp*(sp-s1)*(sp-s2)*(sp-s3))
    return area
               
    
if __name__ == "__main__":
    a = float(input('Enter the first side: '))
    b = float(input('Enter the second side: '))
    c = float(input('Enter the third side: '))
    area = Area(a,b,c)
    print(f"Area of Triangle is {area:.2f}.")
