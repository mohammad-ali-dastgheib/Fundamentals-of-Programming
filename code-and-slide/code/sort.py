def sort(xc,target):
    lb=0
    ub=len(xc)-1
    if lb==ub:
        return -1
    mid=(lb+ub)//2
    if xc[mid]>target:
        xc=xc[:mid]
        sort(xc,target)
    if xc[mid]<target:
        xc=xc[mid+1:]
        sort(xc,target)
    if xc[mid]==target:
        return mid
xc=[1,2,5,7,9,12,15,18,60,68,73,1393]
target=int(input("adad ra vared konid"))
print(sort(xc,target))
