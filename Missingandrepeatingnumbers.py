def missingAndRepeating(arr, n):
    ans = set()
    repeating = 0
    missing = 0
    
    for i in range(1, n + 1):
        if arr.count(i) > 1:
            repeating = i
        elif i not in arr:
            missing = i

    return repeating, missing

arr = [1, 2, 3, 1]
print(missingAndRepeating(arr, len(arr)))
