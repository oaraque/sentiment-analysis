import json
import requests
import csv
import sys

with open(sys.argv[2], 'w') as fout:
    writer = csv.writer(fout, delimiter='\t')
    with open(sys.argv[1], 'r') as fin:
        sentences = fin.readlines()
        response = requests.post('http://sentiment.vivekn.com/api/batch/',
                                data=json.dumps(sentences))
        for i,result in enumerate(response.json()):
            string = sentences[i].strip()
            writer.writerow([result['result'], string])
