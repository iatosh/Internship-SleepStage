import csv
import statistics

csv_file = open("./get_accuracy/acc_yasa_1ch.csv", "r", encoding="utf-8")
f = csv.reader(csv_file, delimiter=",")
lis, c = [], 0
next(f)
for row in f:
    print(row)
    lis.append(float(row[1]))
    c += 1
print(max(lis))
print(min(lis))
print(statistics.mean(lis))
