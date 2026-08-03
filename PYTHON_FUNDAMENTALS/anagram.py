def is_anagram(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()
    freq1 = {}
    freq2 = {}

    #first string frequency counting dict
    for char in str1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1

    #second string frequency counting dict
    for char in str2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1
    print(freq1)
    print(freq2)

    #comparing two dict
    if freq1 == freq2:
        print("ANAGRAM")
    else:
        print("NOT ANAGRAM")

str1 = "silent"
str2 = "listen"
is_anagram(str1,str2)