#Q3.Write a program to check if two strings are a rotation of each other?
def is_rotation(str1, str2):
  if len(str1) != len(str2):
    return False

  concat_str1 = str1 + str1

  return str2 in concat_str1

print(is_rotation("abcde", "cdeab"))  
print(is_rotation("abcde", "abced")) 