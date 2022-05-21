def Multiply_and_greet(*number,**student):
    num=1
    for x in number:
        num*=x
        print(num)
    print(f"Hello{student}")