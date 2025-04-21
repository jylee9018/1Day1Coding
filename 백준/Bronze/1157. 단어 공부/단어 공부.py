from collections import Counter

word = input().upper()

count = Counter(word)
most_common = count.most_common()

if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
    print("?")
else:
    print(most_common[0][0])