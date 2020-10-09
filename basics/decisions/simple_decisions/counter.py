#Ask user for numbers
print("Please enter the first whole number")
first=int(input())

print("Please enter the second whole number")
second=int(input())

print("Please enter the thrid whole number")
third=int(input())

#Counter of odd and even numbers
num_even = 0
num_odd = 0

if (first % 2 == 0):
  num_even += 1
else:
  num_odd += 1

if (second % 2 == 0):
  num_even += 1
else:
  num_odd += 1

if (third % 2 == 0):
  num_even += 1
else:
  num_odd += 1

#Display the result
print("There were {} even and {} odd numbers".format(num_even,num_odd))