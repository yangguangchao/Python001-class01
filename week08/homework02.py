def mymap(func,seq): 
    mapped_seq = [] 
    for eachItem in seq: 
        mapped_seq.append(func(eachItem)) 
    return mapped_seq
def add(x):
    return x+6
    
y=mymap(add,(1,4,6))
print(y)