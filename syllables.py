vowels_list=['а','и','е','ё','о','у','ы','э','ю','я',]

def last_letter(syl,word,k):
	n=True
	while n==True:
		if not any(word[k] in s for s in vowels_list):
			k-=1
		else:
			if not any(word[k-1] in s for s in vowels_list):
				syl[len(syl)-1]=syl[len(syl)-1][0:-1]
				syl.append(word[k-1:])
			else:
				syl.append(word[k:])				
			n=False
	return syl

def syllables(word):
	syl=[]
	c=0
	k=0

	while k<len(word):
		pass
		if any(word[k] in s for s in vowels_list):
			l=False	
			k+=1
			while l==False and k<len(word):
				if any(word[k] in s for s in vowels_list):
					syl.append(word[c:k])
					c=k					
				if k==len(word)-1:
					syl=last_letter(syl,word,k)
				k+=1		
		k+=1
	return syl