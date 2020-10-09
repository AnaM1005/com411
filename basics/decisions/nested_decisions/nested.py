#Ask the user about the type of the book
print("What type of cover does the book have? (hard/soft)")
cover_type=input()

#Display appropriate message
if cover_type == "soft":
  print("Is the book perfect bound?")
  perfect_bound=input()

  if perfect_bound =="Yes":
     print("Soft cover, perfect bound books are very popular!")
  else:
    print("Soft cover, perfect bound books are very popular!")
else:
  print("Books with hard covers can be more expensive!") 