lst = eval(input())
flst = []
f2lst = []
def expanding(lst):
    for i in range(0,len(lst)):
        j = lst[i] - lst[i-1]
        flst.append((j**2)**0.5)
        f2lst.append((j**2)**0.5)
    flst.pop(0)
    f2lst.pop(0)
    
    f2lst.sort()
    
    if(flst==f2lst):
        return True
    else:
        return False
print(expanding(lst))