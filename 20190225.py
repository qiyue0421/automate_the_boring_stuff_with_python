def collatz(number):
    if number % 2 == 0:
        number = number//2
        print(number)
        return(number)
    if number % 2 == 1:
        number = number * 3 + 1
        print(number)
        return(number)


print('enter a num:')
num = int(input())
while True:
    collatz(num)
