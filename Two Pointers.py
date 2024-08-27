#01. Two Pointers Exercises

## 1. Removing duplicates 

def remove_duplicate(arr):
    if len(arr) == 0:
        return 0

    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]

    return i + 1


arr = [1, 2, 2, 4, 5, 5, 8]
length = remove_duplicate(arr)
print(length)  # Output should be 5
print(arr[:length])  # Output should be [1, 2, 4, 5, 8]

## 2. Finding number of pairs for target_sum

def find_sum(arr, target_sum):
    p1 = 0
    p2= len(arr)-1
    n_list=[]

    while p1< p2 :
        current_sum = arr[p1]+arr[p2]

        if current_sum== target_sum :
            n_list.append((arr[p1], arr[p2]))
            p1+=1
            p2-=1

        elif current_sum> target_sum:
            p2-=1
        else:
            p1+=1
    return n_list
arr=[1,2,3,4,5,7,8]
target_sum = 6
print(find_sum(arr, target_sum))

##3. Palindrome Checking

def palindromeCheck(s):
    left = 0
    right = len(s)-1

    while left<right :
        while left<right and not  s[left].isalnum():
            left+=1
        while left<right and not s[right].isalnum():
            right-=1
        if s[left].lower()!=s[right].lower():
            return False

        left+=1
        right-=1

    return True
s= "A man, a plan, a canal: Panama"
print(palindromeCheck(s))







