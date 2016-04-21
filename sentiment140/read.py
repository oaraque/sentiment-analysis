import sys
import csv

def polarity(s):
    if s == 4:
        return 1
    elif s == 2:
        return 0
    elif s== 0:
        return -1

input_, output_ = str(sys.argv[1]), str(sys.argv[2])

with open(output_, 'w') as fout:
    writer = csv.writer(fout, delimiter='\t')
    with open(input_, 'r') as fin:
        reader = csv.reader(fin, delimiter=',')
        for l_i, line in enumerate(reader):
            prediction = polarity(int(line[0]))
            writer.writerow([l_i, prediction])
