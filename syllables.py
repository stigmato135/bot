vowels="аАоОиИеЕёЁэЭыЫуУюЮяЯ"
vowels_list=['а','и','е','ё','о','у','ы','э','ю','я',]

def syllables(word):
	syl=[]
	c=0
	k=0

	while k<len(word):
		if any(word[k] in s for s in vowels_list):
			l=False	
			k+=1
			while l==False and k<len(word):
				if any(word[k] in s for s in vowels_list):
					syl.append(word[c:k])
					c=k					
				if any(word[k] in s for s in vowels_list) and k==len(word)-1:
					c=k
					n=True
					while n==True:
						if not any(word[c] in s for s in vowels_list):
							c-=1
						else:
							if not any(word[c-1] in s for s in vowels_list):
								syl[len(syl)-1]=syl[len(syl)-1][0:-1]
								syl.append(word[c-1:])
							else:
								syl.append(word[c:])				
							n=False
				if not any(word[k] in s for s in vowels_list) and k==len(word)-1:
					c=k
					n=True
					while n==True:
						if not any(word[c] in s for s in vowels_list):
							c-=1
						else:
							if not any(word[c-1] in s for s in vowels_list):
								syl[len(syl)-1]=syl[len(syl)-1][0:-1]
								syl.append(word[c-1:])
							else:
								syl.append(word[c:])				
							n=False
				k+=1		
		k+=1
	return syl