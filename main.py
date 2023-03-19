# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

a = 4
b = 100
c = 400



if year % a == 0:
  if year % b == 0:
    if year % c == 0:
      print("is leap year")
    else:
      print("is not leap year")
  else:
    print("is leap year")
else:
  print("is not leap year")

