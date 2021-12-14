class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return an integer
    
    def canCompleteCircuit(self, A, B):
        count = 0
        n, m = len(A), len(B)
        for i in range(n):
            for i in range(m):
                if A[i] >= B[i] and A[i] != 0:
                    count +=1
                    print(i)
                if A[n-1] <= B[m-1]:
                    count = -1
                    print(i)

        return count

      '''
########################## OR #########################

    def McanCompleteCircuit(self, A, B):
            begin = 0
            total = 0
            fuel = 0
            for i in range(len(A)):
                fuel = fuel + A[i] - B[i]
                if fuel < 0:
                    begin = i+1
                    total = total + fuel
                    fuel = 0
            if total + fuel < 0:
                return -1
            else:
                return begin
    '''      
