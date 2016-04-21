import sys
import csv
from lxml import etree

tree = etree.parse(sys.argv[1])
root = tree.getroot()

def polarity(s):
    if s == 'Positive':
        return 1
    elif s == 'Negative':
        return -1
    elif s == 'Neutral':
        return 0

with open(sys.argv[2], 'w') as fout:
    writer = csv.writer(fout, delimiter='\t')
    for sentence in root[0][0]:
        sentiment = polarity(sentence.attrib['sentiment'])
        writer.writerow([sentence.attrib['id'],sentiment])
