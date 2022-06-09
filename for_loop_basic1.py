num = 0
while num <= 150:
    print(num)
    num = num + 1

num = 5
while num <= 1000:
    print(num)
    num = num + 5

for num in range(1,101):
    if (num % 10 == 0):
        print("Coding Dojo")
    elif (num % 5 == 0):
        print("Coding")
    else:
        print(num)

odds = 0

for a in range(500000):
    if a % 2 != 0:
        odds = odds + a

print(odds)

for count_down in range(2018, 0, -4):
    if count_down % 2 == 0:
        print(count_down)

low_num = 2
high_num = 10
mult = 3

for z in range(low_num,high_num):
    if z % mult == 0:
        print(z)
