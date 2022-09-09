words = "Enter number between 1 to 10 to repeat question. \npress o for exit."
print(words)
enterednum = []
while True:
    number = int(input("Enter number: "))
    if number == 0:
        exit()
    if number <= 11:
        enterednum.append(number)
        print(f"you enter {enterednum} ")
