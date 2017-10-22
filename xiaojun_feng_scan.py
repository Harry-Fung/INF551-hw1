import sys
# Testing GitHub branch
def scan():
	testFile = open(sys.argv[1])
	lines = testFile.readlines()
	given_pos = int(lines[0])
	requests = lines[1].split(',')
	requests = map(int,requests)
	#print "Start Position: ", given_pos
	requests.sort()
	min_request = min(requests) #find the min request track
	max_request = max(requests) #find the max request track
	min_seek = 999
	schedule = []
	seek_time = 0
	temp1_time = 0
	temp2_time = 0
	#print requests
	#find first closest request
	for request in requests:
		diff = abs(given_pos - request)
		if diff < min_seek:
			min_seek = diff
			position = request #store the first closest request position
			time = min_seek
	#print position
	schedule.append(position) #take care of first request
	requests.remove(position) #remove processed request
	#head move to the right first
	if position > int(lines[0]):
		for x in range(position,200):
			if x in requests:
				schedule.append(x) #take care of the processed request
				requests.remove(x) #remove processed request
				#check if finish the whole request
				if len(requests) == 0:
					seek_time = abs(max_request - given_pos)
		temp1_time = 199 - given_pos
		#seek back up from 200 to min if not finish requests
		if len(requests) > 0:			
			for y in range(200,min_request-1,-1):
				if y in requests:
					schedule.append(y) #take care of the processed request
					requests.remove(y) #remove processed request
			temp2_time = abs(199 - y)
			seek_time = temp1_time + temp2_time
		#print "right"
	#head move to the left first
	else:
		for x in range(position,-1,-1):
			if x in requests:
				schedule.append(x)
				requests.remove(x)
				#check if finish the whole request
				if len(requests) == 0:
					seek_time = abs(given_pos - min_request)
		temp1_time = given_pos - 0
		#seek back up from 0 to max if not finish request
		if len(requests) > 0:	
			for y in range(0,max_request+1):
				if y in requests:
					schedule.append(y) 
					requests.remove(y)
			temp2_time = max_request
			seek_time = temp1_time + temp2_time						
		#print "left"
	print schedule
	print seek_time
	print schedule[-1], seek_time
scan()