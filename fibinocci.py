def fibinocci(num):
    if num<=0:
        return []
    ans=[0,1]
    for i in range(num):
        temp=ans[-1]+ans[-2]
        ans.append(temp)
    return ans

#Test Case

num=5
print(fibinocci(num))
    