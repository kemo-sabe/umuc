import re, time

sen_count = 0
wrd_count = 0
syl_count = 0

def syllable_count(word):
	global syl_count
	word = word.lower()
	vowels = "aeiouy"
	if word[0] in vowels:
		syl_count += 1
	for index in range(1, len(word)):
		if word[index] in vowels and word[index - 1] not in vowels:
			syl_count += 1
	if word.endswith("e"):
		syl_count -= 1
	if syl_count == 0:
		syl_count += 1

def sentc_split(phrases):
	text = ''.join(open(phrases).readlines())
	sentences = re.split(r' *[\.\?!;:][\'"\)\]]* +', text)
	outF = open("ManiBrk.txt","w")
	for line in sentences:
		outF.write(line)
		outF.write("\n")
	outF.close()
	newPhras = "ManiBrk.txt"
	#return newPhras

def load(phrases):
	global sen_count
	global wrd_count
	#sentc_split(phrases)
	#newPhras = sentc_split
	with open(phrases, 'r') as f:
		for line in f:
			#print(line)
			sen_count += 1
			wrd_count += len(line.split())
			for word in line:
				#print(word)
				#wrd_count += 1
				syllable_count(word)
					
if __name__ == "__main__":
	start = time.time()
	load("Mani_text_test.txt")
	avg_slb_per_word = syl_count / wrd_count #ASW
	avg_wrd_per_sent = wrd_count / sen_count #ASL
	readability_score = 206.835 - (1.015 * avg_wrd_per_sent) - (84.6 * avg_slb_per_word)
	end = time.time()
	total_time = end - start
	print("Sentence Count = {}".format(sen_count))
	print("Syllable Count = {}".format(syl_count))
	print("Word Count = {}".format(wrd_count))
	print("Average syllable per word Count = {}".format(avg_slb_per_word))
	print("Average word per sentence Count = {}".format(avg_wrd_per_sent))
	print("Readability = {}".format(readability_score))
	print("Finished in = {}".format(total_time))
