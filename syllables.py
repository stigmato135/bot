vowels_list = ['а', 'и', 'е', 'ё', 'о', 'у', 'ы', 'э', 'ю', 'я']


def syllables(word):
    syllables = []
    current_syllable = ""
    for id,letter in enumerate(word):
        current_syllable += letter
        if letter in vowels_list:
            syllables.append(current_syllable)
            current_syllable = ""
            last_letter=id
            last_syl=len(syllables)
    if current_syllable != "":
        syllables[-1] += current_syllable
    for id,letter in enumerate(syllables[-1]):
        if letter in vowels_list :
            last_vowel = id
    for id_syl , syl in enumerate(syllables):
        current_syllable = ""
        print (id_syl)
        for id_letter , letter in enumerate(syl):
            current_syllable += letter
            if (letter == "ъ" or letter == "ь") and (id_syl<len(syllables)-1 or (id_syl==len(syllables)-1 and id_letter < last_vowel )) :
                current_syllable = syllables[id_syl - 1] + current_syllable
                syllables[id_syl - 1] = current_syllable
                syllables[id_syl] = syllables[id_syl][id_letter + 1:]
    return syllables