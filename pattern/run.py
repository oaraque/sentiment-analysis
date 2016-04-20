import csv
import sys
import codecs

from pattern.en import sentiment

input_, output_ = str(sys.argv[1]), str(sys.argv[2])


with codecs.open('/output.txt', 'w') as fout:

    writer = csv.writer(fout, delimiter='\t')
    with codecs.open('/input.txt', 'r') as fin:
        for l_i, line in enumerate(fin):
            line = line.strip()
            result = sentiment(line)[0]
            prediction = None
            if result > 0:
                prediction = 1
            elif result < 0:
                prediction = -1
            elif result == 0:
                prediction = 0
            writer.writerow([l_i, prediction])


