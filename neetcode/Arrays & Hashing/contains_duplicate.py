def contains_duplicate(nums):
    dic = {}
    for i in nums:
        if i in dic:
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1

    for key, val in dic.items():
        # print(key,val)
        if val > 1:
            return True
    return False

nums = [1, 2, 3, 3]
contains_duplicated = contains_duplicate(nums)
contains_duplicated