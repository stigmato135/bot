vowels_list=['а','и','е','ё','о','у','ы','э','ю','я',]

def last_letter(syl,word,letter):
	flag=True
	while flag==True:
		if not any(word[letter] in s for s in vowels_list):
			letter-=1
		else:
			if not any(word[letter-1] in s for s in vowels_list):
				syl[len(syl)-1]=syl[len(syl)-1][0:-1]
				syl.append(word[letter-1:])
			else:
				syl.append(word[letter:])				
			flag=False
	return syl

def syllables(word):
	syl=[]
	vowel=0
	letter=0
	while letter<len(word):
		if any(word[letter] in s for s in vowels_list):
			letter+=1
			while  letter<len(word):
				if any(word[letter] in s for s in vowels_list):
					syl.append(word[vowel:letter])
					vowel=letter					
				if letter==len(word)-1:
					syl=last_letter(syl,word,letter)
				letter+=1		
		letter+=1
	return syl