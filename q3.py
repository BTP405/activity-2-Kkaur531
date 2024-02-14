# (15 points) Write a Python function `wordCount(t)` which retrives data in a text file _t_ and returns a dictionary where the _keys_ are unique words in the files 
# and the corresponding _values_ are lists of line numbers where the words are found in the text.
def wordCount(t):
  word_dict={} #initializes an empty dictionary to store the word occurrences and their respective line numbers.
  with open(t, 'r') as file:
        data = file.readlines()
        #line iterates over each line in the data list, and enumerate is used to get both the line content and its line number. 
        for line_number, line in enumerate(data, start=1):
            words = line.split() #splits the current line into a list of words based on the default whitespace separator.
            for word in words:
                word = word.strip().lower() # removes leading and trailing whitespaces from the word and converts it to lowercase
              #The if statement checks if a word is an existing key in the word_dict, if not, it adds the current line_number to the list, or adds it as a new key with a list containing only the current line_number.
                if word:
                    if word in word_dict:
                        if line_number not in word_dict[word]:
                            word_dict[word].append(line_number)
                    else:
                        word_dict[word] = [line_number]
    return word_dict
