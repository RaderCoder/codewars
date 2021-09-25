def delete_nth(x,n):
    ans=[]
    for o in x:
        if ans.count(o) < n:
            ans.append(o)
    print(ans)

delete_nth([1,1,1,1],2)
delete_nth([20,37,20,21],1)
delete_nth([1,1,3,3,7,2,2,2,2],3)
