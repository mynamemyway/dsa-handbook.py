words_l = [word.strip('.,!?:;-') for word in input().lower().split()]

words_d = {}
for word in words_l:
    words_d.setdefault(words_l.count(word), set()).add(word)

print(*sorted(words_d[min(words_d)]))