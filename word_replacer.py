#   This function censors the text with the second argument.
#   Example if you want to censor 'losing' from 'we are losing' the 'losing'
#   Will be replaced by *'s of the same length.
def censor (text,word):
  replacement = '*' * len(word)

  sentance = []

  for block in text.split():
    if(block == word):
        sentance.append(replacement)
    else:
        sentance.append(block)
  return(" ".join(sentance))


print(censor("we are losing","losing"))
