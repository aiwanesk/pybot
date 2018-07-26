import string

class Parser():
    """ Cut and clean a sentence, and return the main keyword """

    def __init__(self, sentence):
        self.sentence = sentence

    def cut_sentence(self):

        split_sentence = self.sentence.split(" ")
        print(split_sentence)

        punctuation = string.punctuation

        sentence_whitout_punctuation = []
        flag = True

        for word in split_sentence:
            # To delete single punctation mark
            if len(word) == 1 and word in punctuation:
                continue
            
            for lettre in word:
                if lettre not in punctuation:
                    flag = True
                    continue
                else:
                    # if there is punctation mark in the word, split the words
                    word_split = word.split(lettre)
                    for elt in word_split:
                        sentence_whitout_punctuation.append(elt)
                    flag = False
                    break
            
            if flag:
                sentence_whitout_punctuation.append(word)       

        print(sentence_whitout_punctuation)

        return self.sentence + " ok"