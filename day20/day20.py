# CONSTANTS
KEY = 811589153

# STRUCTURES


# GLOBALS


# MAIN
def mix(nums, idx, locs):
    n = nums[idx]
    for _ in range(abs(n)):
        if n > 0 and idx == len(nums) - 1:
            # rotate right then swap right
            nums.insert(0, nums.pop())
            locs.insert(0, locs.pop())
            idx = 0
            nums[idx], nums[idx+1] = nums[idx+1], nums[idx]
            locs[idx], locs[idx+1] = locs[idx+1], locs[idx]
            idx = 1
        elif n < 0 and idx == 0:
            # rotate left then swap left
            nums.append(nums.pop(0))
            locs.append(locs.pop(0))
            idx = len(nums) - 1
            nums[idx], nums[idx-1] = nums[idx-1], nums[idx]
            locs[idx], locs[idx-1] = locs[idx-1], locs[idx]
            idx = len(nums) - 2
        elif n > 0:
            # swap right then rotate right if necessary
            nums[idx], nums[idx+1] = nums[idx+1], nums[idx]
            locs[idx], locs[idx+1] = locs[idx+1], locs[idx]
            idx += 1
            if idx == len(nums) - 1:
                nums.insert(0, nums.pop())
                locs.insert(0, locs.pop())
                idx = 0
        elif n < 0:
            # swap left then rotate left if necessary
            nums[idx], nums[idx-1] = nums[idx-1], nums[idx]
            locs[idx], locs[idx-1] = locs[idx-1], locs[idx]
            idx -= 1
            if idx == 0:
                nums.append(nums.pop(0))
                locs.append(locs.pop(0))
                idx = len(nums) - 1
    print(n, nums, locs)


def coords(nums):
    idx_0 = nums.index(0)
    rsf = 0
    for n in 1000, 2000, 3000:
        n += idx_0
        rsf += nums[n % len(nums)]
    return rsf


def part1(lines) -> int:
    nums = [int(n) for n in lines]
    # map initial location in nums to current location
    locs = [i for i in range(len(nums))]
    for i in range(len(nums)):
        idx = locs.index(i)
        mix(nums, idx, locs)
    print(nums)
    return coords(nums)


def part2(lines) -> int:
    nums = [int(n) * KEY for n in lines]
    locs = [i for i in range(len(nums))]
    for _ in range(10):
        print('round: ' + str(nums))
        for i in range(len(nums)):
            idx = locs.index(i)
            mix(nums, idx, locs)
    return coords(nums)


def main():
    with open("test.txt") as f:
        # print("Part 1 Test: " + str(part1(f.readlines())))
        print("Part 2 Test: " + str(part2(f.readlines())))
    with open("input.txt") as f:
        pass
        # print("Part 1 Input: " + str(part1(f.readlines())))
        # print("Part 2 Input: " + str(part2(f.readlines())))


if __name__ == '__main__':
    main()
