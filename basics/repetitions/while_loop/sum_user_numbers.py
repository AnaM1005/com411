#Ask user for a number
print ("How many numbers should I sum up?")
number_to_sum = int(input())

#Declare the control variable
summed = 0

print()

#Sum numbers
total = 0

while (summed < number_to_sum):
  print("Please enter number", summed, "of", number_to_sum, ":")
  number = int(input())
  total = total + number
  summed = summed + 1

#Display result
print("The answer is", total)
