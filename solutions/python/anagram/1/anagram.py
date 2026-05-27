def find_anagrams(word, candidates):
    validated_anagrams = []
    for candidate in candidates:
        if word.lower() == candidate.lower():
            continue
        if len(candidate) != len(word):
            continue
        verification = list(candidate.lower())
        for char in word:
            if char.lower() in verification:
                verification.remove(char.lower())
            else:
                continue
        if verification == []:
            validated_anagrams.append(candidate)
    return validated_anagrams
            