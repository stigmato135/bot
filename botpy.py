from syllables import syllables


def substitution(word):
	syl=syllables(word)
	print (syl)
	if len(syl)==2:
		for i in syl[0]:
			if i.lower()=='о'or i.lower()=='ё':
				syl[0]='хуё'
			elif i.lower()=='а':
				syl[0]='хуя'
			elif i.lower()=='у':
				syl[0]='хую'
			elif i.lower()=='э' or i.lower()=='е':
				syl[0]='хуе'
			elif i.lower()=='ы' or i.lower()=='и':
				syl[0]='хуи'
	else:
		if syl[1]=='ишк':
			syl[0]='ху'
		else:
			i=syl[1][-1]
			if i.lower()=='о' or i.lower()=='ё':
				syl[1]='ё'+syl[1][:-1]
			elif i.lower()=='а':
				syl[1]='я'+syl[1][:-1]
			elif i=='у':
				syl[1]='ю'+syl[1][:-1]
			elif i.lower()=='э' or i.lower()=='е':
				syl[1]='е'+syl[1][:-1]
			elif i.lower()=='ы' or i.lower()=='и':
				syl[1]='и'+syl[1][:-1]
			syl[0]='ху'
	word=''
	word = ''.join(syl)
	print (word)
	return word
	