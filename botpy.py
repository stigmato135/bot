from syllables import syllables,vowels_list

def bonding(syl, letter):
    syl[0] = 'ху'
    if letter.lower() == 'ё':
        syl[0] = syl[0]+'ё'
    elif letter.lower() == 'а':
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
    length = len(syl)
    if length == 5 or length == 6:
        del syl[0]
    if length == 7 or length == 8:
        del syl[0:2]
    for id, letter in enumerate(syl[0]):
        if letter in vowels_list:
            new_id = id
            i = letter
    if length == 2:
        if syl[1][0] not in vowels_list:
            syl = bonding(syl, i)
        else:
            syl[0] = 'ху'
    else:
        if syl[1] == 'ишк':
            syl[0] = 'ху'
        elif new_id!=0 :
            syl=bonding(syl,i)
        elif new_id==0 and len(syl[1])>1:
            syl[1]=syl[1][1:]
            syl=bonding(syl,i)
        else:
            del syl[1]
            syl=bonding(syl)

    word = ''
    word = ''.join(syl)
    print (word)

    return word
