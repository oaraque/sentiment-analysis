import csv
import sys

with open(sys.argv[2], 'w') as fout:
	writer = csv.writer(fout, delimiter='\t')
	with open(sys.argv[1], 'r') as fin:
		for line in fin:
			l = line.strip().replace('.','')+'.'
			writer.writerow([l])
