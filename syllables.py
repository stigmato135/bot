vowels_list=['а','и','е','ё','о','у','ы','э','ю','я',]

'''
def syllables(word):
    syllables = []
    current_syllable = ""
    for letter in word:
        current_syllable += letter
        if letter in vowels_list:
            syllables.append(current_syllable)
            current_syllable = ""
    if current_syllable !="":
        syllables[-1] += current_syllable
    return syllables
'''

def syllables(word):
    syllables = []
    current_syllable = ""
    for letter in word:
        current_syllable += letter
        if letter in vowels_list:
            syllables.append(current_syllable)
            current_syllable = ""
    if current_syllable !="":
        syllables[-1] += current_syllable
    for id_syl,syl in enumerate(syllables):
        current_syllable = ""
        for id_letter,letter in enumerate(syl):
            current_syllable += letter
            if letter == "ъ" or letter == "ь":
                current_syllable = syllables[id_syl - 1] + current_syllable
                syllables[id_syl - 1] = current_syllable
                syllables[id_syl] = syllables[id_syl][id_letter + 1:]
    return syllables