a = [1,2,3,4,5,10,50,100, -1000]
print (a)
b=a[0]
for i in range (len(a)):
    if b>a[i]:
        b=a[i]
print (b)

c=0
for i in range (len(a)):
   c = c+a[i]

print (c)
d=c/len(a)
print(d)

print(sum(a)/len(a))
