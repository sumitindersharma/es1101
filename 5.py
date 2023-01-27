word = str(input("enter a word = "))
inverse = word[::-1]
print(inverse)

n=int(input("enter a no. = "))
a=int(input("enter the lower value of range = "))
b=int(input("enter the upper value of range = "))
c=b-a
count = 0
while count<=c:
    if(a%n==0):
        print(a)
    else:
        print()
    count=count+1
    a=a+1


a = int(input("enter 1st side of triangle = "))
b = int(input("enter 2nd side of triangle = "))
c = int(input("enter 3rd side of triangle = "))
s = (a + c + b) / 2
if c >= a + b:
    print("enter a valid triangle")
elif b >= a + c:
    print("enter a valid triangle")
elif a >= b + c:
    print("enter a valid triangle")
else:
    area = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)
    print(area)


n = 5
for i in range(n):
    for j in range(i):
        print("* ", end=" ")
    print(" ")
for i in range(n, 0, -1):
    for j in range(i):
        print("* ", end=" ")
    print(" ")




size = 5
letter = 65
for i in range(0, size + 1):
    for j in range(0, i):
        character = chr(letter)
        print(character, end='')
        letter += 1
    print()


a = int(input("enter the lower value of range = "))
b = int(input("enter the upper value of range = "))
for number in range(a, b + 1):
    count = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            count = count + 1
            break

    if count == 0 and number != 1:
        print("%d" % number, end=" ")


for i in range(1,500):
    if(i%7==0):
        if(i%11==0):
            print(i)


for i in range (1,11):
    i = int(input("enter a number = "))
    if (i>=0):
        if i == 0:
            print("zero")
        else:
            print("positive number")
    else:
        print("negative number")
    if(i%2) == 0:
        print(str(i) + " is even")
    else:
        print(str(i) + " is odd")



a = input(str("enter a line : "))


def word_count(line):
    counts = dict()
    words = line.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


print(word_count(a))
