def words_in_text(text):
    if text ==1:
        return 1
    else:
        for i in range(0,len(text)):
            return len(text)


text1 = input("enter a word")
print(words_in_text(text1))