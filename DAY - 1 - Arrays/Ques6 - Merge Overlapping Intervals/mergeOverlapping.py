class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if(len(intervals)==0):
            return []
        intervals = sorted(intervals, key=lambda x:x[0])
        last = intervals[0][1]
        start = intervals[0][0]
        
        res = []
        
        for i in range(1, len(intervals)):
            if(last>=intervals[i][0]):
                if(intervals[i][1]<last):
                    pass
                else:
                    last = intervals[i][1]
            else:
                res.append([start, last])
                start = intervals[i][0]
                last = intervals[i][1]
        res.append([start, last])
        return res