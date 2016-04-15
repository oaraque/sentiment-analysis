import csv
import codecs

from vaderSentiment.vaderSentiment import sentiment as vaderSentiment

def to_unicode(obj, encoding='utf-8'):
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj = unicode(obj, encoding)
    return obj


with codecs.open('/input.txt', 'r') as fin:
    lines = fin.readlines()

with codecs.open('/output.txt', 'w') as fout:
    writer = csv.writer(fout, delimiter='\t')
    for l_i, line in enumerate(lines):
        result = vaderSentiment(line)
        prediction = None
        if result['compound'] > 0:
            prediction = 1
        elif result['compound'] < 0:
            prediction = -1
        elif result['compound'] == 0:
            prediction = 0
        writer.writerow([l_i, prediction])
