print("Program started!")
print("Please enter an ASCII code between 32 and 126:")
code=abs(int(input()))

if (code >= 32 and code <= 126):
  ascii_letter = chr(code)
  print("The character represented by the ASCII value {} is:{}.". format(code, ascii_letter))
else:
  print("The character cannot be displayed.")

print ("Program ended!")