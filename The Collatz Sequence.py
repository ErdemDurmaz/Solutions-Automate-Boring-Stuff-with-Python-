#page 101 The Collatz Sequence
def collatz(number):
    if number % 2 == 0:
        print("This number",number," is even")
        floor = number // 2
        print(floor)
        if floor == 1:
            print(" Collatz sequence is initiated")
            quit()
        
    else:
        print("This number",number," is odd")
        calc = 3 * number + 1
        print(calc)
        if calc == 1:
            print(" Collatz sequence is initiated")
            quit()
        
while True:
    try:
        usrinp = int(input("Enter the number: "))
    except:
        print("Something went wrong")
    collatz(usrinp)