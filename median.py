# Function to print the median value in a list.
# If the list is an even length, the index either side are averaged.
# E.g. [6,5,1,2] the list is sorted to [1,2,5,6]
# Then the (2+5)/2.0 = 3.5 so the median is 3.5.
# If the list is odd it's more simple.

def median(lst_to_calc):
  lst_to_calc = sorted(lst_to_calc)
  # For corner case if list len is 1
  if len(lst_to_calc) == 1:
    return lst_to_calc[0]
  else:
    middle = (len(lst_to_calc) / 2.0)

    if middle % 1 == 0:
      middle_l = int(middle - 1)
      middle_r = int(middle)
      median = (lst_to_calc[middle_l] + lst_to_calc[middle_r]) / 2.0
    else:
      middle = int(middle - 0.5)
      median = lst_to_calc[middle]

  return median

print(median([6,8,12,2,23]))
