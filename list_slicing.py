#   List Slicing allows you to access elements of a list in a concise manner.
#   Syntax is [start:end:stride]
#   Default is [beginning_of_list:end_of_list:one_at_a_time]

list_to_slice = [x for x in range(1,16)]    #   Print list 1-15

#   So start is 5, end is 10, printing every 2.
print (list_to_slice[5:10:2])

#   No start of finished specified so default beginning to end used.
#   Printing every 3.
print(list_to_slice[::3])

#   Printing defaults. So same as doing list_to_slice[0:15:1]
print (list_to_slice[::])


#   To print reverse use negative numbers.
print (list_to_slice[::-1])
