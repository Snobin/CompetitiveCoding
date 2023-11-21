class Solution():
    def merge(self,intervals):
        intervals.sort()
        output=[intervals[0]]
        for start,end in intervals[1:]:
            lastend=output[-1][1]
            if start<=lastend:
                output[-1][1]=max(end,lastend)
            else:
                output.append([start,end])
        return output

ans=Solution()
#Test Case
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(ans.merge(intervals))
            
        