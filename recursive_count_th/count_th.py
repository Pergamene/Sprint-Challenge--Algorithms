'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
  if len(word) == 0:
    return 0
  return _count_th_recursive(word, 0)

def _count_th_recursive(word, start):
  index = word.find('th', start)
  if index == -1:
    return 0
  return 1 + _count_th_recursive(word, index + 1)
