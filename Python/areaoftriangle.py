import math
def Area(s1,s2,s3):
    if(s1 == s2 == s3):
        area = (math.sqrt(3)/4) * math.pow(s1,2)
        print(f"Area of given Equilateral Triangle: {area:.2f}")

    elif(s1 == s2 or s2 == s3 or s1 == s3):
        if(s1 == s2):
            area = 0.5 * s1 * s3
            print(f"Area of given Isosceles Triangle: {area:.2f}")
        elif(s2 == s3):
            area = 0.5 * s2 * s1
            print(f"Area of given Isosceles Triangle: {area:.2f}")
        elif(s1 == s3):
            area = 0.5 * s3 * s2
            print(f"Area of given Isosceles Triangle: {area:.2f}")
    else:
        sp = (s1 + s2 + s3) / 2
        area = math.sqrt(sp*(sp-s1)*(sp-s2)*(sp-s3))
        print(f"Area of given Triangle: {area:.2f}")
               
    
if __name__ == "__main__":
    a = float(input('Enter the first side: '))
    b = float(input('Enter the second side: '))
    c = float(input('Enter the third side: '))
    Area(a,b,c)
