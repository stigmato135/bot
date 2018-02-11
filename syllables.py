vowels_list=['а','и','е','ё','о','у','ы','э','ю','я',]
consoles_list=['без','бес','в','во','вз','взо','вс','вне','внутри','воз','возо','вос','все','вы','до','за','из','изо',
               'ис','испод','к','кое','кой','меж','междо','между','на','над','надо','наи','не','небез','небес','недо',
               'ни','низ','низо','нис','о','об','обо','обез','обес','около','от','ото','па','пере','по','под','подo',
               'поза','после','пра','пре','пред','предо','преди','при','про','противо','раз','разо','рас','роз','рос',
               'с','со','сверх','среди','су','сыз','тре','у','чрез','через','черес']

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

def consoles(word):
    new_word=""
    for id,letter in enumerate(word):
        new_word+=letter
        if new_word in consoles_list  and id<7:
            word=word[id+1:]
            break
    return word