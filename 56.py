
56. Merge Intervals
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].


# my complicated solution TT, different sort direction made so many difference
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def isoverlapped(self, a, b):
      #  print type(a)
        print a.start,a.end,b.start,b.end
        if (a.end>=b.start and b.end>=a.end) or (b.end>=a.start and a.end>=b.end):
            print min(a.start,b.start),max(a.end,b.end)
            return Interval(min(a.start,b.start),max(a.end,b.end))
        else:
            return None
            
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        newInterval = []
        length = len(intervals)
        i = 1
        if intervals == []:
            return []
        
        f = lambda x:x.end
        intervals = sorted(intervals, key=f)
        cur = intervals[0]
        
        while(i!=length):
            la = intervals[i]
            newl = self.isoverlapped(cur,la)
            if (newl == None):
                newInterval.append(cur)
                cur = la
            else:
                cur = newl
            i+=1
        newInterval.append(cur)

        i = len(newInterval)
        if i <2:
            return newInterval
        finalInternal = []
        cur = newInterval[i-1]
        i = i-2
        while(i>=0):
            la = newInterval[i]
           # print list(cur), list(la)
            newl = self.isoverlapped(cur,la)
            if (newl == None):
                finalInternal.append(cur)
                cur = la
            else:
                cur = newl
            i-=1    
        finalInternal.append(cur)
        
        return finalInternal        

    #    return newInterval   
        
            
# smart solution
'''
class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x.start)
        result = []
        for interval in intervals:
            if len(result) == 0 or result[-1].end < interval.start:
                result.append(interval)
            else:
                result[-1].end = max(result[-1].end, interval.end)
        return result
'''
