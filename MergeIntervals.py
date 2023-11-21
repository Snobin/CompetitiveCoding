class Solution():
    def merge(self,intervals):
        #Sort the input list
        intervals.sort()
        #Set interval variable as first element in sorted list interval
        output=[intervals[0]]
        # print(output)
        #from second element in sorted list interval where start=first(1) ele and end =last(3) ele
        for start,end in intervals[1:]:
            # print("ans",start,end)
            # set lastend as the last ele in the last added output list
            lastend=output[-1][1]
            # print("lastend",lastend)
            # check first element in next is less than last element in previous 
            if start<=lastend:
                #if it is true set last element in prev as maximum of lastend and end
                output[-1][1]=max(end,lastend)
            else:
                #if it is false append the entire list element in output list
                output.append([start,end])
        #Return output list
        return output

ans=Solution()
#Test Case
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(ans.merge(intervals))
            
        