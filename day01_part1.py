import sys

with open(sys.argv[1], 'r') as f:
	totals = []
	t = 0
	for line in f.readlines():
		if line=="\n":
			totals.append(t)
			t = 0
			continue
		t += int(line.strip("\n"))

max_calories = max(totals)
max_calories_index = totals.index(max_calories)

print(max_calories, max_calories_index)	
