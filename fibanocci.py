f=0
s=1
n=int(input("Enter the no of terms:"))
print(f,s,end=" ")
for i in range(n):
    t=f+s
    f=s
    s=t
    print(t,end=" ")
    