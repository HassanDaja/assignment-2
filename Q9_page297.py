def vowels_counter(sentence):
    vowel=0
    consonants=0
    vowels=["a","A","e","E","I","i","o","O","u","U"]
    letters=[]
    for x in sentence:
        letters.append(x)
    for x in letters:
        for vow in vowels:
            if x==vow:
                vowel+=1
    consonants=len(sentence)-vowel
    print(f"The number of vowels are:{vowel}")
    print(f"The number of consonants are:{consonants}")


