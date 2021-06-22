def can_jump(nums):
    '''
    Leetcode 0055 (Medium): Jump Game
    '''
    goal = len(nums) - 1
    for i in range(len(nums) -2, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return goal == 0