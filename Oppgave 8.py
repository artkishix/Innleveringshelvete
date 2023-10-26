for i in range (len([1, 2, 3, 4, 1, 2, 3, 4])):
    print(f'{i+1} sitter {[i for i in range (1, 21)][sum([1, 2, 3, 4, 1, 2, 3, 4][:i]) : sum([1, 2, 3, 4, 1, 2, 3, 4][:i + 1])]}')