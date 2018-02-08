from syllables import syllables


def last_letter(word):
	syl=syllables(word)
	print (syl)
	if len(syl)==2:
		for i in syl[0]:
			if i=='о' or i=='О' or 'ё' or 'Ё':
				syl[0]='хуё'
			elif i=='а' or i=='А':
				syl[0]='хуя'
			elif i=='у' or i=='У':
				syl[0]='хую'
			elif i=='э' or i=='Э' or i=='е' or i=='Е':
				syl[0]='хуе'
			elif i=='Ы' or i=='Ы' or i=='и' or 'И':
				syl[0]='хуи'
	else:
		if syl[1]=='ишк':
			syl[0]='ху'
		else:
			i=syl[1][0]
			if i=='о' or i=='О':
				syl[1]='ё'+syl[1][1:]
			elif i=='а' or i=='А':
				syl[1]='я'+syl[1][1:]
			elif i=='у' or i=='У':
				syl[1]='ю'+syl[1][1:]
			elif i=='э' or i=='Э' or i=='е' or i=='Е':
				syl[1]='е'+syl[1][1:]
			elif i=='Ы' or i=='Ы' or i=='и' or 'И':
				syl[1]='и'+syl[1][1:]
			syl[0]='ху'
	word=''
	word = ''.join(syl)
	print (word)
	return word