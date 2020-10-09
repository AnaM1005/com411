print("Please enter the first whole number.")
first=int(input())

print("Please enter the second whole number.")
second=int(input())

if (first < second):
  print("{} is smaller than {}".format(first,second))
elif (first>second):
  print("{} is smaller than {}".format(second,first))
else:
  print("These numbers are equals.")  

