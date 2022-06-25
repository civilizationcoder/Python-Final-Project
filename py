m = ([1,'a',['cat'],2],[[[3]],'dog'],4,5)

new_m = []

def flatten(x):
    for i in m:
        res1=new_m.append(i)
    return new_m

print(flatten(m))
