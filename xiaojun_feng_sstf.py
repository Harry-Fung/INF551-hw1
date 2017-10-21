import sys

def sstf():
	testFile = open(sys.argv[1])
	lines = testFile.readlines()
	current_pos = int(lines[0])
	requests = lines[1].split(',')
	requests = map(int,requests)
	#print "Start Position: ", current_pos
	#print requests
	min_seek = 999
	schedule = []
	seek_time = 0
	requests.sort()
	#print requests
	#print current_pos
	while len(requests) > 0:
		#find the shortest distance from current position
		for request in requests:
			if abs(current_pos - request) < min_seek:
				min_seek = abs(current_pos - request)
				min_position = request #get the min position
				time = min_seek #get the min time
		current_pos = min_position #update current position
		#print min_position	
		seek_time = seek_time + time
		schedule.append(min_position) 	
		requests.remove(min_position) #removed processed request
		min_seek = 999 #reset the min_seek after process each request
		#print "Requests: ", requests
	print schedule
	print seek_time
	print min_position, seek_time
sstf()