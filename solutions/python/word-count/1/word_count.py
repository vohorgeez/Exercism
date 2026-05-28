import re

def count_words(sentence):
    count = dict()
    for word in filter(lambda x: x, re.split(r"[_.:!?,\t\n &@$%^]+", sentence)): #the weirdest lambda i've ever used
        sample = word.lower().strip("'")
        if sample == '':
            continue
        if sample not in count.keys():
            count[sample] = 1
        else:
            count[sample] += 1
    return count