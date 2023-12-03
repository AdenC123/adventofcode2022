# CONSTANTS


# STRUCTURES


# GLOBALS


# MAIN
def mix(nums, idx, locs):
    # print(nums[idx], nums, locs)
    new_idx = (idx + nums[idx])
    if nums[idx] < 0:
        new_idx -= 1
    new_idx %= len(nums)
    if idx < new_idx:
        for i in range(idx, new_idx):
            next_i = (i + 1) % len(nums)
            nums[i], nums[next_i] = nums[next_i], nums[i]
            locs[i], locs[next_i] = locs[next_i], locs[i]
    else:
        for i in range(idx, (new_idx+1) % len(nums), -1):
            next_i = (i - 1) % len(nums)
            nums[i], nums[next_i] = nums[next_i], nums[i]
            locs[i], locs[next_i] = locs[next_i], locs[i]

    # if next_idx > idx:
    #     for i in range(idx, next_idx):
    #         next_i = (i + 1) % len(nums)
    #         nums[i], nums[next_i] = nums[next_i], nums[i]
    #         locs[i], locs[next_i] = locs[next_i], locs[i]
    # elif idx > next_idx:
    #     for i in range(idx, next_idx, -1):
    #         next_i = (i - 1) % len(nums)
    #         nums[i], nums[next_i] = nums[next_i], nums[i]
    #         locs[i], locs[next_i] = locs[next_i], locs[i]

    # for i in range(idx, (idx + n + offset) % len(nums)):
    #     next_i = (i + 1) % len(nums)
    #     nums[i], nums[next_i] = nums[next_i], nums[i]
    #     locs[i], locs[next_i] = locs[next_i], locs[i]

    # new_idx = (idx + nums[idx]) % len(nums)
    # for i in range(idx + 1, new_idx + 1):
    #     prev_i = (i - 1) % len(nums)
    #     nums[prev_i] = nums[i]
    #     og_i = locations[i]
    #     locations[og_i] = prev_i
    # nums[new_idx] = n
    # og_idx = locations[idx]
    # locations[og_idx] = new_idx


def coords(nums):
    idx_0 = nums.index(0)
    rsf = 0
    for n in 1000, 2000, 3000:
        n += idx_0
        # print(nums[n % len(nums)])
        rsf += nums[n % len(nums)]
    return rsf


def part1(lines) -> int:
    nums = [int(n) for n in lines]
    # map initial location in nums to current location
    locs = [i for i in range(len(nums))]
    for i in range(len(nums)):
        idx = locs.index(i)
        mix(nums, idx, locs)
    # print(nums)
    return coords(nums)


def part2(lines) -> int:
    return 0


def main():
    with open("test.txt") as f:
        print("Part 1 Test: " + str(part1(f.readlines())))
        print("Part 2 Test: " + str(part2(f.readlines())))
    with open("input.txt") as f:
        print("Part 1 Input: " + str(part1(f.readlines())))
        print("Part 2 Input: " + str(part2(f.readlines())))


if __name__ == '__main__':
    main()
