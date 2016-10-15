import random
import heapq


def main():
    nums = [random.randint(1, 100000) for i in range(10000)]
    largest_nums = heapq.nlargest(20, nums)
    smallest_nums = heapq.nsmallest(20, nums)
    return [(l + s) for l, s in zip(largest_nums, smallest_nums)]

if __name__ == "__main__":
    main()
