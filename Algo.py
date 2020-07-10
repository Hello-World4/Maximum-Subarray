def maxSubArray(arr): #complexity O(n^2)
    max = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum > max:
                max = sum
    return max

def maxSubArray2(arr): #Kadane’s Algorithm o(n)
    max1 = 0
    max2 = 0
    for i in range(len(arr)):
        max1 += arr[i]
        if max1> max2:
            max2 = max1
        if max1 < 0:
            max1 = 0
    return max2

def maxSubArray3(arr): #Kadane’s Algorithm o(n)
    current_sum = arr[0]
    max1 = arr[0]
    for i in range(1,len(arr)):
        current_sum = max(current_sum + arr[i], arr[i])
        max1 = max(current_sum, max1)
    return max1


if __name__ == "__main__":
    a = [1,-3,2,1,-1]
    print(maxSubArray(a))
    print(maxSubArray2(a))
    print(maxSubArray3(a))