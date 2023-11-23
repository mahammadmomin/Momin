# list
#append 
i=["momin",1,2,3]
i.append("python")
print(i)

#extend
i=["momin","cell no"]
i.extend([9542774631])
print(i)

#count
m=[7,7,9,4,7,3,6,2,4,1,1,9,3,3,9,]
print(m.count(9))

#remove
a=["momin","mosapet"]
a.remove('mosapet')
print(a)

#pop
s=[2,4,42,32,6,57,44,]
s.pop(3)
print(s)

#index
a=[2,4,42,32,6,57,44,]
print(a.index(6))

#insert
m=[2,4,42,32,6,57,44,]
m.insert(2,"hello")
print(m)


#loop
for i in [2,4,42,32,6,57,44,]:
    print(i)


#tuple
c= (1,23,43,12,3,4,6,7,)
print(min(c))
print(max(c))
print(sum(c))
print(len(c))

#concatination
t1=("momin")
t2=("mahammad")
print(t1+t2)

#repitation
m=("python program")
print(m*5)

#iteration
m=("python program")
for i in m:
    print(i)


#membership
m=(5,3,6,2,7,3,8,9,2)
print(7 in m)
print(1 not in m)


t1=(1,2,3)
t2=(3,4,5)
print(t1 not in t2)
print(t1 is t2)
 