def find_anagrams(word, candidates):
    result = []
    word = word.lower()
    for i in candidates:
        candidate = i.lower()
        if candidate != word:
            if sorted(candidate) == sorted(word):
                result.append(i)
    return result  