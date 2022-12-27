'''
numbers = []

for n in num:
    num = int(input("Enter five numbers: "))
    numbers.append(num)
print("Largest number: ",max(numbers))
print("Smallest number: ",min(numbers))
'''

lst = []
#num = int(input('How many numbers: '))
for n in range(1,6):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))