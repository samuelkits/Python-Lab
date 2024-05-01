file=open("alphabets","w+")
st="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n=int(input("enter the number of alphabets in a line: "))
for i in range(len(st)):
    file.write(f"{st[:n:1]}\n")
    if st==st[-1]:
        break
    else:
        st=st[n::]
        file.seek(0)
        r=file.read()
        file.flush()
print(r)
