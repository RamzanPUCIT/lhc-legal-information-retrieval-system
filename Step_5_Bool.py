index = {
    "illegal": [1, 3, 7],
    "detention": [1, 2],
    "court": [1, 4, 5]
}

AND  = lambda a,b: list(set(index.get(a,[])) & set(index.get(b,[])))
OR   = lambda a,b: list(set(index.get(a,[])) | set(index.get(b,[])))
NOT  = lambda a,n: list(set(range(1,n+1)) - set(index.get(a,[])))

print("AND:", AND("illegal","detention"))
print("OR :", OR("illegal","court"))
print("NOT:", NOT("detention",10))
