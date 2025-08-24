''''Given a sentence with numbers representing a word’s location in the 
sentence, embedded within each word, and return the sorted sentence. '''
sentence = input('Enter the sentence: ')
words = sentence.split()
numbers='0123456789'
def num_words(word):
    numbers='0123456789'
    number=''
    for char in word:
        if char in numbers:
            number = number + char
    if number == '':       
        return 0    
    return int(number)
    
for i in range(len(words)):
    for j in range(i+1,len(words)):
        if num_words(words[i]) > num_words(words[j]):
            words[i],words[j]=words[j],words[i]
cleaned=[]
for word in words:
    new_word =''
    for ch in word:
        if ch not in numbers:
            new_word = new_word + ch
    cleaned.append(new_word)
ans =' '.join(cleaned)
print(ans)
