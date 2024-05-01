def is_happy_number(num):
  seen = set()
  while num != 1 and num not in seen:
   seen.add(num)
   num = sum(int(i)**2 for i in str(num))
   return num == 1
number = int(input("Enter a number: "))
if is_happy_number(number):
    print(number," is a Happy Number")
else:
    print(number," is not a Happy Number")
