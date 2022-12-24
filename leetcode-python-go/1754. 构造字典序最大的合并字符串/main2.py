word1 = "abcabc"
word2 = "abdcaba"

def largestMerge(word1: str, word2: str) -> str:
	n=len(word1)
	m=len(word2)
	ans=[]
	i=0
	j=0
	while i<=n-1 or j<=m-1:
		if i>=n or j>=m:
			if i>=n:
				ans.append(word2[j])
				j+=1
			else:
				ans.append(word1[i])
				i+=1
		elif word1[i]>word2[j]:
			ans.append(word1[i])
			i+=1
		elif word1[i]<word2[j]:
			ans.append(word2[j])
			j+=1
		elif word1[i]==word2[j]:
			g=1
			while True:
				if i+g>=n or j+g>=m:
					if i+g>=n:
						ans.append(word2[j])
						j+=1
						break
					else:
						ans.append(word1[i])
						i+=1
						break
				elif word1[i+g]>word2[j+g]:
					ans.append(word1[i])
					i+=1
					break
				elif word1[i+g]<word2[j+g]:
					ans.append(word2[j])
					j+=1
					break                        
				else:
					g+=1
	return "".join(ans)

print(largestMerge(word1, word2))