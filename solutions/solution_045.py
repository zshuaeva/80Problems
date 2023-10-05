# Complete the make_sentences function that accepts three
# lists.
#   * subjects contains a list of subjects for three-word sentences
#   * verbs contains a list of verbs for three-word sentences
#   * objects contains a list of objects for three-word sentences
# The make_sentences function should return all possible sentences
# that can be made from the words in each list
#
# Examples:
#   * subjects: ["I"]
#     verbs:    ["play"]
#     objects:  ["Portal"]
#     returns:  ["I play Portal"]
#   * subjects: ["I", "You"]
#     verbs:    ["play"]
#     objects:  ["Portal", "Sable"]
#     returns:  ["I play Portal", "I play Sable",
#                "You play Portal", "You play Sable"]
#   * subjects: ["I", "You"]
#     verbs:    ["play", "watch"]
#     objects:  ["Portal", "Sable"]
#     returns:  ["I play Portal", "I play Sable",
#                "I watch Portal", "I watch Sable",
#                "You play Portal", "You play Sable"
#                "You watch Portal", "You watch Sable"]
#
# There is pseudocode to guide you. Make sure you understand
# what's going on, here, before continuing.

def make_sentences(subjects, verbs, objects):
    # sentences = new empty list
    sentences = []                                      # solution
    # for each subject in subjects
    for subject in subjects:                            # solution
        # for each verb in verbs
        for verb in verbs:                              # solution
            # for each object in objects
            for object in objects:                      # solution
                # sentence = subject + " " + verb + " " + object
                sentence = subject + " " + verb + " " + object      # solution
                # append sentence to sentences
                sentences.append(sentence)              # solution
    # return sentences
    return sentences                                    # solution
    # pass                                              # problem
