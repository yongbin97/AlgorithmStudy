import sys
from collections import Counter


word = sys.stdin.readline().strip()
word = word.upper()

counter = Counter(word)
common = counter.most_common(2)
if len(common) > 1 and common[0][1] == common[1][1]:
    print("?")
else:
    print(common[0][0])

