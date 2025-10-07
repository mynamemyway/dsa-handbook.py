n = int(input())

l = [list(range(1, i + 1)) for i in range(1, n + 1)]

# for i in range(1, n + 1):
#     l.append(list(range(1, i + 1)))
    
print(*l, sep='\n')
