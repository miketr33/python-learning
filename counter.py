#   This function counts the number of times an item (specified in 2nd argument)
#   appears in the sequence.

def count(sequence, item):
  my_lst = sequence
  counter = 0
  for elem in range (len(my_lst)):
    if my_lst[elem] == item:
      counter = counter + 1

  return counter


# Example, count all the 2's
tst_lst = [1,3,2,2,2,6,3,7,2,4,2,96,22,42,2]

print(count(tst_lst,2))
