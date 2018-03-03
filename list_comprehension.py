#   List comprehension is an elegant way to define & create a list. A substitute
#   for the labd function as well as functions map(), filter() and reduce()

#   Example of a list that is populated by number 1-5
new_list = [x for x in range(1,6)]

#   New list ranging from 1-5 then all numbers doubled.
doubles = [x * 2 for x in range(1,6)]

#   Create a list with all numbers doubled, but only store the ones that are
#   divisable by 3.
doubles_by_3 = [x * 2 for x in range(1,6) if (x * 2) % 3 == 0]

print(new_list, doubles, doubles_by_3)
