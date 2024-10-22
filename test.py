# firs exercise
a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))

max = ""
if a > b and a > c :
    max = a
elif b > a and b > c :
    max = b
else:
    max = c

print(max)


# second
word = input("enter a word")
count = 0
dzaynavorner = "aeouiAEOUI"
for char in word:
    if char in dzaynavorner:
        count += 1

print(count)

# fourth
number = int(input("Enter a number: "))
digits = str(number)
num_digits = len(digits)
sum_of_powers = 0


for digit in digits:
    sum_of_powers += int(digit) ** num_digits

if sum_of_powers == number:
    print("it is an Armstrong number!")
else:
    print("it is not an Armstrong number.")


# fifth
list = [12,34,53,21,4,77]
max = list[0]
for i in range(len(list)) :
    if list[i] > max:
        max = list[i]

list.remove(max)
secondMax = list[0]
for i in range(len(list)) :
    if list[i] > secondMax:
        second = list[i]

print(secondMax)


# third??






