from calc_func import do_addition,do_subtraction

def main():
    num1=int(input())
    num2=int(input())
    print("select operation:")
    print("1.Add")
    print("2.Subtract")
    choice=input()
    if choice=='1':
        print("Addition is = ")
        print(do_addition(num1,num2))
    if choice=='2':
        print("Subtraction is = ")
        print(do_subtraction(num1,num2))
if __name__=="__main__":
    main()
