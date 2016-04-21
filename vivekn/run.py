import json
import requests
import csv
import sys

def polarity(s):
    if s == 'Positive':
        return 1
    elif s == 'Negative':
        return -1
    elif s == 'Neutral':
        return 0

with open(sys.argv[2], 'w') as fout:
    writer = csv.writer(fout, delimiter='\t')
    with open(sys.argv[1], 'r') as fin:
        sentences = fin.readlines()
        response = requests.post('http://sentiment.vivekn.com/api/batch/',
                                data=json.dumps(sentences))
        for i,result in enumerate(response.json()):
            string = sentences[i].strip()
            prediction = polarity(result['result'])
            writer.writerow([i, prediction])
