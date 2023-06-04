# def subsets(nums: list[int]) -> list[list[int]]:
#     res = []
#     def backtrack(start, subset):
#         res.append(subset[:])
#         print(res)
#         for i in range(start, len(nums)):
#             subset.append(nums[i])
#             backtrack(i + 1, subset)
#             subset.pop()
            
#     backtrack(0, [])
#     return res


def subsets(nums: list[int]) -> list[list[int]]:
    result = []

    def back(idx, subset):
        if idx >= len(nums):
            result.append(subset[:])
            return
        
        subset.append(nums[idx])
        back(idx + 1, subset)

        subset.pop()
        back(idx + 1, subset)
    
    back(0, [])
    return result
print(subsets([1,2,3]))