# c = int(c*(line-i)/i)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = []
        
        for i in range(1, numRows+1):
            c = 1
            temp = []
            for j in range(1, i+1):
                temp.append(c)
                c = int(c*(i-j)/j)
            res.append(temp)
            
        return res