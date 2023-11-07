def eliminateMaximum(dist, speed):
    times=[(dist[i]-1)//speed[i] for i in range(len(dist))]
    times.sort()
    for i in range(len(times)):
        if times[i]<i:
            return i
    return len(dist)


#Test Case

dist = [1,1,2,3]
speed = [1,1,1,1]
print(eliminateMaximum(dist,speed))