## Program to check whether two strings are anagram or not

def check_anagram(word1, word2):

	word1 = sorted(word1)
	word2 = sorted(word2)

	if len(word1) == len(word2) and word1 == word2:
		print "The words are anagrams"

	else:
		print "The words are not anagrams"


check_anagram("listen","silent")