#   dont change the code below
row1 = ["  ","  ","  "]
row2 = ["  ","  ","  "]
row3 = ["  ","  ","  "]
map = [row1, row2,row3]
print(f"{row1}\n{row2}\n{row3}")
postiton = input("where do you want to put the treasure? ")
#   dont change the code above

#write your code below this row
horizonal = position[0] #2
vertical = position[1] #3

map[vertical - 1][horizonal - 1] = "x"

#write your code above this row

#   dont change the code below
print(f"{row1}\n{row2}\n{row3}")
