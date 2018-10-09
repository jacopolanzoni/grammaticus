#!/usr/bin/python

import time

punctuation_marks = ['.', ',', ':', ';', '\'', ')', '(', '!', '?']
vocabulary = {}
word_count = 0

initial_time = time.time()

for line in open('texts/ovi_met_3_316_510.txt', 'r'):
    for word in line.split():
        word = word.lower()
        while word[0] in punctuation_marks:
            word = word[1:]
        while word[-1] in punctuation_marks:
            word = word[:-1]
        word_count += 1
        if word in vocabulary:
            vocabulary[word] += 1
        else:
            vocabulary[word] = 1

duration = time.time() - initial_time
message = 'Sorted {0} words in {1:.2g} seconds ({2:.2g} milliseconds/word).'
print(message.format(word_count, duration, duration/word_count*1000))

initial_time = time.time()

for vocabulary_entry in sorted(vocabulary.items(), key=lambda kv: kv[1]):
    print('{:>2}: {}'.format(vocabulary_entry[1], vocabulary_entry[0]))

duration = time.time() - initial_time
message = 'Purged in {0:.2g} milliseconds.'
print(message.format(duration*1000))
