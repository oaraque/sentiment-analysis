import csv
import sys
import codecs

from textblob import TextBlob

input_, output_ = str(sys.argv[1]), str(sys.argv[2])


with codecs.open('/output.txt', 'w') as fout:

    writer = csv.writer(fout, delimiter='\t')
    with open('/input.txt', 'r') as fin:
        for l_i, line in enumerate(fin):
            result = TextBlob(line).sentiment.polarity
            prediction = None
            if result > 0:
                prediction = 1
            elif result < 0:
                prediction = -1
            elif result == 0:
                prediction = 0
            writer.writerow([l_i, prediction])


