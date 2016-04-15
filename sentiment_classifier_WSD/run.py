import sys
from string import punctuation
from  unicodecsv import *
from senti_classifier import senti_classifier

input_data = sys.argv[1]
output_data = sys.argv[2]


def to_unicode(obj, encoding='utf-8'):
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj = unicode(obj, encoding)
    return obj

def arg_max(iterable):
    return max(enumerate(iterable), key=lambda x: x[1])[0]

def polarity(index):
    if index == 0:
        return '1'
    elif index == 1:
        return '-1'

def clean(text, exclude):
    return ''.join(ch for ch in text if ch not in exclude)

exclude = set(punctuation)

# Write to output
with open(sys.argv[2], 'w') as fout:
    writer = UnicodeWriter(fout, delimiter='\t')
    # Read dataset
    with open(sys.argv[1], 'r') as fin:
        for l_i, line in enumerate(fin):
            line = to_unicode(line).strip()
            line = clean(line, exclude)
            pos_neg = senti_classifier.polarity_scores([line])
            pol = polarity(arg_max(pos_neg))
            writer.writerow([l_i, pol])
