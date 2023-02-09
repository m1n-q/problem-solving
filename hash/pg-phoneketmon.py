#hash

from collections import Counter

def solution(nums: list):
    size = len(nums)
    amount = size // 2
    counter = Counter(nums)

    if len(counter) <= amount:
        answer = len(counter)
    else:
        answer = amount
    return answer
