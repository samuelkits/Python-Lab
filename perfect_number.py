n = int(input("enter a number: "))
def isPerfectNumber(num):
   pn = 0
   for i in range(1, num):
     if num % i == 0:
       pn += i
       if (pn == num):
         return True
       return False
print(isPerfectNumber(n))