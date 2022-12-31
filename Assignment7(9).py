#Q.9 Write a program to reverse a stack.
def reverse_stack(stack):
  if not stack:
    return
  bottom = get_and_remove_bottom(stack)
  reverse_stack(stack)

  stack.append(bottom)

def get_and_remove_bottom(stack):

  if len(stack) == 1:
    return stack.pop()

  top = stack.pop()

  bottom = get_and_remove_bottom(stack)

  stack.append(top)

  return bottom


stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print(stack)  