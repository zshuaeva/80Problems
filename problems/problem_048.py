# Write a function that meets these requirements.
#
# Name:       count_word_frequencies
# Parameters: sentence, a string
# Returns:    a dictionary whose keys are the words in the
#             sentence and their values are the number of
#             times that word has appeared in the sentence
#
# The sentence will contain now punctuation.
#
# This is "case sensitive". That means the word "Table" and "table"
# are considered different words.
#
# Examples:
#    * sentence: "I came I saw I learned"
#      result:   {"I": 3, "came": 1, "saw": 1, "learned": 1}
#    * sentence: "Hello Hello Hello"
#      result:   {"Hello": 3}

## FUNCTION PSEUDOCODE
# function count_word_frequencies(sentence):
    # words = split the sentence
    # counts = new empty dictionary
    # for each word in words
        # if the word is not in counts
            # counts[word] = 0
        # add one to counts[word]
    # return counts
def count_word_frequencies(sentence):
    words = sentence.split(" ")
    counts = {}
    for i in words:
        if i not in counts:
            print(i)
            counts[i] = 0
        counts[i] += 1

    return counts
