import random
import heapq

from guppy import hpy


def main():
    nums = []
    for _ in range(10000):
        nums.append(random.randint(1, 100000))

    hp = hpy()
    print 'heapy after appending 10000 random integers'
    h = hp.heap()
    print(h)
    print

    for _ in xrange(10000, 20000):
        nums.append(random.randint(1, 100000))
    print 'heapy after appending 20000 random integers'
    h = hp.heap()
    print(h)
    print

    largest_nums = heapq.nlargest(20, nums)
    smallest_nums = heapq.nsmallest(20, nums)
    result = []
    for l, s in zip(largest_nums, smallest_nums):
        result.append(l + s)
    print 'heapy after creating the result list'
    h = hp.heap()
    print(h)
    print
    return result

if __name__ == "__main__":
    main()
