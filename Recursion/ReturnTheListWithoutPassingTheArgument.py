def findAllIndex(arr, target, index):
    if index == len(arr):
        return []
    ans = []
    if arr[index] == target:
        ans.append(index)

    ansFromBelow = findAllIndex(arr, target, index + 1)
    ans.extend(ansFromBelow)
    return ans


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(findAllIndex(list, 5, 0))
