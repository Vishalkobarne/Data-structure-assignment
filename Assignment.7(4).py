
#Q4. Write a program to print the first non-repeated character from a string?
def first_non_repeated(s):
  char_count = {}
  for c in s:
    if c in char_count:
        char_count[c] += 1
    else:
        char_count[c] = 1
  for c in s:
    if char_count[c] == 1:
        return c

print(first_non_repeated("abcdefghijklmnopqrstuvwxyz")) 
print(first_non_repeated("aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz")) 