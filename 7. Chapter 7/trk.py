'''
def main():
    num = int(input("Enter number for multiplication table: "))
    for i in range(1, 11):
        print(f"{num} * {i} = {mul(num, i)} ")


def mul(a, b):
    return a*b

main()
'''

'''
l1 = ["harry", "sohan", "sachin", "rahul"]

for name in l1:
    if name.startswith("s"):
        print("hello, " + name)
'''



'''
num = int(input("Enter number for whether prime or not: "))

count = 0
for i in range(1, num):
    if num % i == 0:
        count += 1

if count == 1:
    print(f"{num} is prime number. ")
else:
    print(f"{num} is not prime number. ")
'''




'''
n = int(input("enter number: "))
sum = 0
for i in range(1, n+1):
    sum = sum + i

print("sum is : ", sum)
'''



'''
for i in range(4):
    print("*" * i)
'''


'''
n = 4
for i in range(n):
    print(" " * (n-i-1), end = "")
    print("*" * (2*i-1), end = "")
    print(" " * (n*i-1))
'''








