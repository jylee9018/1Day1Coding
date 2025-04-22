def count_word(word):
    counts = {}
    for i in range(len(word)):
        if word[i] not in counts.keys():
            counts[word[i]] = 1
        else:    
            if (0 <= i + 1 < len(word)) and (word[i] == word[i + 1]):
                counts[word[i]] += 1
            if (0 <= i - 1 < len(word)) and (word[i - 1] == word[i]):
                counts[word[i]] += 1
            else:
                return False
    return True


N = int(input())

count = 0
for _ in range(N):
    word = input()
    if count_word(word) == True:
        count += 1

print(count)
