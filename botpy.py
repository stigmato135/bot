from syllables import syllables,consoles,vowels_list

def bonding(syl):
    i = syl[0][-1]
    if i.lower() == 'о' or i.lower() == 'ё':
        syl[1] = 'ё' + syl[1]
    elif i.lower() == 'а':
        syl[1] = 'я' + syl[1]
    elif i == 'у':
        syl[1] = 'ю' + syl[1]
    elif i.lower() == 'э' or i.lower() == 'е':
        syl[1] = 'е' + syl[1]
    elif i.lower() == 'ы' or i.lower() == 'и':
        syl[1] = 'и' + syl[1]
    syl[0] = 'ху'
    return syl

def substitution(word):
    syl = syllables(word)
    print (syl)
    print (consoles(word))
    if len(syl) == 2:
        if syl[1][0] not in vowels_list:
            for i in syl[0]:
                if i.lower() == 'о' or i.lower() == 'ё':
                    syl[0] = 'хуё'
                elif i.lower() == 'а':
                    syl[0] = 'хуя'
                elif i.lower() == 'у':
                    syl[0] = 'хую'
                elif i.lower() == 'э' or i.lower() == 'е':
                    syl[0] = 'хуе'
                elif i.lower() == 'ы' or i.lower() == 'и':
                    syl[0] = 'хуи'
        else:
            syl[0] = 'ху'
    else:
        for id,letter in enumerate(syl[1]):
            if letter in vowels_list:
                new_id=id
                i=letter
        if syl[1] == 'ишк':
            syl[0] = 'ху'
        elif new_id!=0 :
            syl=bonding(syl)
        elif new_id==0 and len(syl[1])>1:
            syl[1]=syl[1][1:]
            syl=bonding(syl)
        else:
            del syl[1]
            syl=bonding(syl)

    word = ''
    word = ''.join(syl)
    print (word)

    return word
