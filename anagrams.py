def isAnagram(word1,word2):
    word1 = sorted(word1.lower())
    word2 = sorted(word2.lower())
    return "".join(word1) == "".join(word2)

