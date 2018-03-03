#   This program removes duplicate ints, leaving one copy of each in a list.
def remove_duplicates(list_to_clean):
  result_lst = []
  dup_found = False

  for item in range(len(list_to_clean)):    # Runs through each item in the list to list_to_clean
      for contents in range(len(result_lst)):   # Runs through and checks if item is a duplicate.
          if list_to_clean[item] == result_lst[contents]:
              dup_found = True
              break
          else:
              dup_found = False
      if dup_found == False:
          result_lst.append(list_to_clean[item])    # Item only appended if not a duplicate

  return result_lst

list_to_check = [5,4,4,2,5]
print(remove_duplicates(list_to_check))
