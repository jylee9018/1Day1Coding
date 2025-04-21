word = input().lower()

word_count = dict()
for i in range(len(word)):
    if word[i] not in word_count:
        word_count[word[i]] = 0
    word_count[word[i]] += 1

answer = []
max_count_value = max(word_count.values())
for c in word_count.keys():
    if word_count[c] == max_count_value:
        answer.append(c)

if len(answer) > 1:
    print("?")
else:
    print(answer[0].upper())