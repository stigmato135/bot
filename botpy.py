vowels="аАоОиИеЕёЁэЭыЫуУюЮяЯ"
vowels_list=['а','и','е','ё','о','у','ы','э','ю','я',]
def last_letter(word):
	syllables=[]
	c=0
	k=0

	while k<len(word):
		if any(word[k] in s for s in vowels_list):
			l=False	
			k+=1
			while l==False and k<len(word):
				if any(word[k] in s for s in vowels_list):
					syllables.append(word[c:k])
					c=k					
				if any(word[k] in s for s in vowels_list) and k==len(word)-1:
					c=k
					n=True
					while n==True:
						if not any(word[c] in s for s in vowels_list):
							c-=1
						else:
							if not any(word[c-1] in s for s in vowels_list):
								syllables[len(syllables)-1]=syllables[len(syllables)-1][0:-1]
								syllables.append(word[c-1:])
							else:
								syllables.append(word[c:])				
							n=False
				if not any(word[k] in s for s in vowels_list) and k==len(word)-1:
					c=k
					n=True
					while n==True:
						if not any(word[c] in s for s in vowels_list):
							c-=1
						else:
							if not any(word[c-1] in s for s in vowels_list):
								syllables[len(syllables)-1]=syllables[len(syllables)-1][0:-1]
								syllables.append(word[c-1:])
							else:
								syllables.append(word[c:])				
							n=False
				k+=1		
		k+=1

	del c
	del k
	print (syllables)
	if len(syllables)==2:
		for i in syllables[0]:
			if i=='о' or i=='О' or 'ё' or 'Ё':
				syllables[0]='хуё'
			elif i=='а' or i=='А':
				syllables[0]='хуя'
			elif i=='у' or i=='У':
				syllables[0]='хую'
			elif i=='э' or i=='Э' or i=='е' or i=='Е':
				syllables[0]='хуе'
			elif i=='Ы' or i=='Ы' or i=='и' or 'И':
				syllables[0]='хуи'
	else:
		if syllables[1]=='ишк':
			syllables.pop(0)
			syllables.insert(0, 'ху')
		else:
			i=syllables[1][0]
			if i=='о' or i=='О':
				syllables[1]='ё'+syllables[1][1:]
			elif i=='а' or i=='А':
				syllables[1]='я'+syllables[1][1:]
			elif i=='у' or i=='У':
				syllables[1]='ю'+syllables[1][1:]
			elif i=='э' or i=='Э' or i=='е' or i=='Е':
				syllables[1]='е'+syllables[1][1:]
			elif i=='Ы' or i=='Ы' or i=='и' or 'И':
				syllables[1]='и'+syllables[1][1:]
			syllables.pop(0)
			syllables.insert(0, 'ху')

	word=''
	word = ''.join(syllables)
	print (word)
	return word