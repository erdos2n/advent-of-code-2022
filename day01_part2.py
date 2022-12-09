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

top_three = sorted(totals)[-3:]
print(top_three)
print(sum(top_three))
