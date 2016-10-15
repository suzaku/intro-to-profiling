import random
import heapq


@profile
def main():
    nums = []
    for _ in range(10000):
        nums.append(random.randint(1, 100000))
    for _ in xrange(10000, 20000):
        nums.append(random.randint(1, 100000))
    largest_nums = heapq.nlargest(20, nums)
    smallest_nums = heapq.nsmallest(20, nums)
    result = []
    for l, s in zip(largest_nums, smallest_nums):
        result.append(l + s)
    return result

if __name__ == "__main__":
    main()
