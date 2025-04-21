# word = input().upper()

# word_count = dict()
# for i in range(len(word)):
#     if word[i] not in word_count:
#         word_count[word[i]] = 0
#     word_count[word[i]] += 1

# answer = []
# max_count_value = max(word_count.values())
# for c in word_count.keys():
#     if word_count[c] == max_count_value:
#         answer.append(c)

# if len(answer) > 1:
#     print("?")
# else:
#     print(answer[0])

#----------

# dict.get()을 활용하여 보다 간단히 카운트가 가능하다.
word = input().upper()
word_count = {}

for c in word:
    word_count[c] = word_count.get(c, 0) + 1

max_count = max(word_count.values())
common = [k for k, v in word_count.items() if v == max_count]

print("?" if len(common) > 1 else common[0])
