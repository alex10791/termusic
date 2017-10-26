
import sys
from time import sleep

timings = {
	"W" : 16,
	"H" : 8,
	"Q" : 4,
	"I" : 2,
	"S" : 1
}

if len(sys.argv) == 2:
	full_time = 0.05
	songfile = sys.argv[1]
if len(sys.argv) == 3:
	full_time = float(sys.argv[1])
	songfile = sys.argv[2]

f = open(songfile)


for line in iter(f):
	notes = list(line.strip())
	for note in notes:
		if note in timings:
			sys.stdout.write("\a")
			sys.stdout.flush()
			sleep(full_time*timings[note])
f.close()


