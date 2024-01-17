#1
my_list = ["apple", "banana", "orange", "grapes"]
for fruit in my_list:
    print(fruit)
length = 0
for i in my_list:
    length = length+1
    print(length)
#2
numbers_1 = [1, 2, 3, 4, 4]
total = sum(numbers_1)
print("Sum of numbers is:", total)
numbers_2 = [5, 6, 7]
new_list = numbers_1 + numbers_2
print(new_list)
#3
maximum = max(new_list)
print("The maximum number in the list is", maximum)
minimum = min(new_list)
print("The minimum number in the list is", minimum)
count_of_4 = new_list.count(4)
print("No.of times 4 occured is", count_of_4)
#4
list_names = ["Taylor", "Selena", "Gigi"]
for name in list_names:
    print("Hello", name)
def even(n):
    return n % 2 == 0
even_numbers = list(filter(even, new_list))
print("Even numbers are", even_numbers)
#5
list_words = ["Bike", "Car", "Bus", "Jeep", "Cycle"]
slice_words = list_words[1:4]
print("The first three words are", slice_words)
reversed_list = list_words[::-1]
print("The reversed list is", reversed_list)
#6
squares = [x ** 2 for x in range(10)]
print("squares of numbers are:", squares)
even_numbers = [x for x in new_list if x % 2 == 0]
print("Even numbers are::", even_numbers)
#7
list_names.sort()
print("Names in alphabetical order:", list_names)
new_list.sort()
new_list.reverse()
print("Numbers in descending order:", new_list)
#8
for x in new_list:
    if new_list.count(x) > 1:
        new_list.remove(x)
        print(new_list)
list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 2, 3, 4, 7]
list_3 = []



