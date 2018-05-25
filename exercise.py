lowerCaseVowel = ("a","e","i","o","u")
x = 0
vowel_count  = 0;
s = 'a'
while(x < len(s) ):
	if(s[x] in lowerCaseVowel):
		vowel_count = vowel_count + 1
	x = x+1
print(vowel_count)
