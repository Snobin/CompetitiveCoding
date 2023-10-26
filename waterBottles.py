def numWaterBottles(numBottles,numExchange):
    result=0
    temp=numBottles
    while numBottles>=numExchange:
        sum=numBottles//numExchange
        rem=numBottles%numExchange
        numBottles=sum+rem
        result+=sum
    return result+temp
    
#Test Case
x=15
y=3
output=numWaterBottles(x,y)
print(output)