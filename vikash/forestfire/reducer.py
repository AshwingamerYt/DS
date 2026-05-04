import sys

current_month = None
total = 0
count = 0

for line in sys.stdin:
    month, temp = line.strip().split('\t')
    temp = float(temp)

    if current_month == month:
        total += temp
        count += 1
    else:
        if current_month:
            print(current_month, total / count)
        current_month = month
        total = temp
        count = 1

if current_month:
    print(current_month, total / count)