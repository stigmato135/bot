from syllables import syllables,vowels_list

def bonding(syl, letter):
    syl[0] = 'ху'
    if letter.lower() == 'ё':
        syl[0] = syl[0]+'ё'
    elif letter.lower() == 'а' or letter.lower() == 'я':
        syl[0] = syl[0]+'я'
    elif letter.lower() == 'у':
        syl[0] = syl[0] + 'ю'
    elif letter.lower() == 'э' or letter.lower() == 'е' or letter.lower() == 'о':
        syl[0] = syl[0] + 'е'
    elif letter.lower() == 'ы' or letter.lower() == 'и':
        syl[0] = syl[0] + 'и'
    return syl

def substitution(word):
    syl = syllables(word)
    print (syl)
    for slog in syl:
        for letter in slog:
            if letter == " ":
                return ("Введите одно слово")
    if len(syl)==1:
        return ("Введите слово минимум из двух слогов")
    length = len(syl)
    if length == 5 or length == 6:
        del syl[0]
    if length == 7 or length == 8:
        del syl[0:2]
    for  letter in syl[0]:
        if letter in vowels_list:
            i = letter
    if syl[1][0] not in vowels_list:
        syl=bonding(syl,i)
    elif len(syl[1])==1:
        del syl[1]
        syl = bonding(syl, i)
    else:
        syl[0] = 'ху'
    word = ''
    word = ''.join(syl)
    print (word)

    return word

