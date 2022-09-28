txt = open("paragraph.txt", "r")
words = txt.readline().split(" ")
word_counts = {}
for word in words:
    if "." in word:
        print(word)
        word = word.replace(".", "")
        print(word)
    if "," in word:
        print(word)
        word = word.replace(",", "")
        print(word)
    if "-" in word:
        splitted = word.split("-")
        for w in splitted:
            try:
                if word_counts[w]:
                    word_counts[w] = word_counts[w] + 1
            except:
                word_counts[w] = 1
        pass
    else:
        try:
            if word_counts[word]:
                word_counts[word] = word_counts[word] + 1
        except:
            word_counts[word] = 1
print(word_counts)
txt.close()
