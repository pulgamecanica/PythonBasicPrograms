def area(a, b):
    return a*b

print(area(b=10, a=10)) #The parameters can be declared

#infinite arguments
def mean(*args): # Could be any name after  '*' but by conventions -args
    return sum(args) / len(args)

print(mean(10,30,143,134,134,412,123,0,212))

#Queued arguments
def mean2(**kwargs): #Keywords args (such as  args-> a=smthg)
    return kwargs

print (mean2(a=1, b = 2, c = 3))