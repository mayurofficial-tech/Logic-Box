print("Welcome To The Pattern Generator and number Analyzer!")

while True:
    print("Select an Option:-")
    print("1. Generate a pattern")
    print("2.Analyze a range of numbers")
    print("3.Exit")
    n=int(input("Enter the choice:-"))
    if n==1:
        print("Pattern:-")
        for i in range(1,6):
            for j in range(i):
                print("* ",end="")
            print()
    if n==2:
        sumofnumber=0
        strat=int(input("Enter the start of the range:-"))
        end=int(input("Enter the end of the range:-"))
        for i in range(strat,end+1):
            if i%2==0:
                print(f"Number {i} is Even")
            else:
                print(f"Number {i} is Odd")
            sumofnumber+=i
        print(f"sum of all numbers from {strat} to {end} is:-{sumofnumber}")

    if n==3:
        print("Exiting the program. Goodbye!")
        break