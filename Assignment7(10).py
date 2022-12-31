#Q10.Write a program to find the smallest number using a stack.
def find_smallest(stack):
  if not stack:
    return None

  smallest = stack[-1]
  for num in stack:
    if num < smallest:
      smallest = num

  return smallest


stack = [5, 1, 3, 2, 4]
print(find_smallest(stack))  