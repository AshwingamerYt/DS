import sys

for line in sys.stdin:
    data = line.strip().split(',')
    if len(data) > 8:
        month = data[2]
        temp = data[8]
        print(f"{month}\t{temp}")