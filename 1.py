def sorting(wordslist):
    new_list = sorted(wordslist, key = len, reverse = True)
    return new_list

def vowels(word):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for char in word:
        if char in vowels:
            word = word.replace(char, '')
    return word

# Create list of words
with open('RandomText.txt','r') as file:
    wordslist = file.read().split()

# Remove commas and dots
wordslist = [s.replace(',', '') for s in wordslist] 
wordslist = [s.replace('.', '') for s in wordslist] 

# Convert to lowercase
wordslist = [word.lower() for word in wordslist]

# Remove duplicate words
new_list = []
for word in wordslist:
    if word not in new_list:
        new_list.append(word)

wordslist = new_list
number_of_words = len(wordslist)
wordslist = sorting(wordslist)



# Print the 5 longest words
print(" The 5 longest words of the text (reversed and without vowels)\n")
for i in range(5):
    
    # Remove vowels
    wordslist[i] = vowels(wordslist[i])

    #Reverse the word
    wordslist[i] = wordslist[i][::-1]

    print("     ",i+1,"--->", wordslist[i])

