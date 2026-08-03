def longest_word(words):
    longest = 0
    long_word = ""
    for word in words:
        if len(word) > longest:
            longest = len(word)
            long_word = word
    print(long_word,longest)


words = ["python", "machine", "learning", "AI", "programming"]

longest_word(words)