
def reverse_string(string):
 
  string=''
  index = len(string)
  while index > 0:
      string += string[ index - 1 ]
      index = index - 1
    return string
  print(reverse_string('1234abcd'))
  