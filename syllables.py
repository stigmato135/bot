vowels_list=['а','и','е','ё','о','у','ы','э','ю','я',]


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