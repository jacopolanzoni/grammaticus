import time


class Grammaticus:

    punctuation_marks = ['.', ',', ':', ';', '\'', ')', '(', '!', '?']

    def __init__(self):
        self.word_count = 0
        self.vocabulary = {}

    def read(self, file):
        initial_time = time.time()
        for line in open(file, 'r'):
            for word in line.split():
                word = word.lower()
                while word[0] in Grammaticus.punctuation_marks:
                    word = word[1:]
                while word[-1] in Grammaticus.punctuation_marks:
                    word = word[:-1]
                self.word_count += 1
                if word in self.vocabulary:
                    self.vocabulary[word] += 1
                else:
                    self.vocabulary[word] = 1
        duration = time.time() - initial_time
        message = 'Sorted {0} words in {1:.2g} seconds ({2:.2g} milliseconds/word).'
        print(message.format(self.word_count, duration, duration/self.word_count*1000))

    def sort_words(self):
        initial_time = time.time()
        for vocabulary_entry in sorted(self.vocabulary.items(), key=lambda kv: kv[1]):
            print('{:>2}: {}'.format(vocabulary_entry[1], vocabulary_entry[0]))
        duration = time.time() - initial_time
        message = 'Purged in {0:.2g} milliseconds.'
        print(message.format(duration*1000))
