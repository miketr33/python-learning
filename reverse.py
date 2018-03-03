# Working function. Pass it a string and it will write it backwards.

def reverse (text):
    num = len(text) - 1
    r_str = ""

    while (num >= 0):
        r_str = r_str + text[num]
        num = num - 1
    return r_str

print(reverse("abcd"))
