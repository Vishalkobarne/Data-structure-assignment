#Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?
def find_pairs_with_sum(arr, sum):
  pairs = set()
  for i in range(len(arr)):
    diff = sum - arr[i]
    if diff in arr and (arr[i], diff) not in pairs:
      pairs.add((arr[i], diff))

  return pairs
  
arr = [1, 2, 3, 4, 5]
sum = 5
pairs = find_pairs_with_sum(arr, sum)
print(pairs)



