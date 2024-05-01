def myfun(*args):
 last_input = args[-1]
 divisors = [i for i in range(1, last_input + 1) if last_input % i == 0]
 print(f"{last_input} : {divisors}")
myfun(6, 7, 8)
myfun(1, 2, 5, 7, 9)
myfun(1, 3, 5, 7, 9, 12)