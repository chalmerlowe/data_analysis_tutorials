myname = input('provide your name: ')
counter = 0

while counter != 10:
    print(myname)
    counter = counter + 1

myage = input('provide your age: ')
myage = int(myage) + 1
for num in range(myage):
    print(num)
