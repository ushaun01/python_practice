a="usha umesh nazare"
#output=ahsu hsemu erazan

b=a.split(" ")
print(b)
list=[]
for i in b:
    list.append(i[::-1])
print(list)
c=" ".join(list)
print(c)