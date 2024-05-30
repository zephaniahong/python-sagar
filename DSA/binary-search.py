# O(log(n))
# non-decreasing
target = 10
arr = [5, 10, 11, 12, 15, 20, 29]

# 2^? = n
# O(1) arr[3]
# O(log(n))
# O(n)
# O(nlog(n))
# O(n^2)
# O(2^n)


def binary_search(array, target):
    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = (start + end) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1


def bs(arr, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return bs(arr, target, start, mid - 1)
    else:
        return bs(arr, target, mid + 1, end)


print(bs(arr, 20, 0, len(arr) - 1))


# iterative
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        # mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


# print(binary_search(arr, target))


# recursive
# def bs(arr, target, start, end):
#     if end < start:
#         return -1
#     mid = (start + end) // 2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] > target:
#         return bs(arr, target, start, mid - 1)
#     else:
#         return bs(arr, target, mid + 1, end)


# print(bs(arr, target, 0, len(arr) - 1))

# Time complexity
# 2^x = n
# log_2(n)

# peak finding (finding the peak, given there is increase and decrease...)
# [2, 5, 7, 9, 15, 23, 8, 6]
# [73, 42, 13, 5, -17, -324]
# [100, 42, 17, 3, 8, 92, 234]
# O(log(n))


# hint: K_HOURS = [1, 2, 3, 4, 5, .... X]
# arr = [5, 1, 3, 10]
# Koko loves to eat bananas. There are N piles of bananas, the i-th pile has piles[i] bananas. The guards have gone and will come back in H hours.
#
# Koko can decide her bananas-per-hour eating speed of K. Each hour, she chooses some pile of bananas, and eats K bananas from that pile.
# If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.
#
# Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.
#
# Return the minimum integer K such that she can eat all the bananas within H hours.

# O(nlog(n))


def koko(bananas, K, H):
    pass


x = koko(arr, 3, 10)
x = koko(arr, 3, 20)


# My ATTEMPT
def peak_finding(arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if (arr[mid] - arr[mid - 1]) > 0 and (
            mid == len(arr) - 1 or (arr[mid] - arr[mid + 1])
        ) > 0:  # Confused about this part. What if peak is the 1st element or last element.
            return mid

        elif (
            arr[mid + 1] - arr[mid] > 0
        ):  # If next element is bigger than current mid element, take 2nd half
            start = mid + 1

        elif arr[mid - 1] - arr[mid] > 0:
            end = mid - 1  # If previous element is bigger than

    return -1


print(peak_finding([2, 5, 7, 9, 15, 23, 8, 6]))
print(peak_finding([73, 42, 13, 5, -17, -324]))
print(peak_finding([100, 42, 17, 3, 8, 92, 234]))


def koko(bananas, H):
    start = 1
    end = max(bananas)

    while start <= end:
        mid = (start + end) // 2

        total_hours = 0

        for i in bananas:

            total_hours += -(-i // mid)

            if total_hours <= H:

                end = mid - 1

            else:

                start = mid + 1

    return start


arr = [5, 1, 3, 10]

x = koko(arr, 10)
print("koko:", x)

y = koko(arr, 20)
print("koko:", y)
