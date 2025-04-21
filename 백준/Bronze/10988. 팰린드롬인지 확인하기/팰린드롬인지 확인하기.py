word = input()

def check_word(word):
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True

if not check_word(word):
    print(0)
else:
    print(1)