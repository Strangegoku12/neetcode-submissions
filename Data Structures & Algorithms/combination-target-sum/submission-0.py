class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        k=[]
        df=[]
        index=0
        lenindex=len(nums)
        def sums(index,trg):
            if trg == 0:
                return k.append(df.copy())
            if index>=lenindex or trg <0:
                return
            df.append(nums[index])
            sums(index,trg - nums[index])
            df.pop()
            sums(index+1,trg)
        
        sums(0,target)
        return k


        