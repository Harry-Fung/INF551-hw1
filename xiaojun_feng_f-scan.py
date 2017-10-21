import sys


def fscan():
    testFile = open(sys.argv[1])
    lines = testFile.readlines()
    cur_position = int(lines[0])
    requests = lines[1].split(',')
    requests = map(int, requests)
    new_list = []
    min_seek = 999
    schedule = []
    seek_time = 0
    temp1_time = 0
    temp2_time = 0
    total_time = 0
    # print "Start Position: ", cur_position
    # print requests
    # split the list into sublists of 10 requests each
    # and store the new list
    new_list = [requests[i:i + 10] for i in range(0, len(requests), 10)]
    # print new_list
    # Begin scan the first list in new list
    for requests_list in new_list:
        # print requests_list
        max_request = max(requests_list)  # get max from each list in new list
        min_request = min(requests_list)  # get min from each list in new list
        # print "current position: ", cur_position
        # print "max and min: ", max_request, min_request
        # start the scan process
        # find first closest request
        for request in requests_list:
            diff = abs(cur_position - request)
            if diff < min_seek:
                min_seek = diff
                position = request  # store the first closest request position
            # time = min_seek #in case of future use, get min seek time
        min_seek = 999  # reset min_seek after first closest request is found
        print cur_position, position
        schedule.append(position)  # take care of first request
        requests_list.remove(position)  # remove processed request
        # head move to the right first
        if position > cur_position:
            # print "right"
            for x in range(position, 200):
                if x in requests_list:
                    schedule.append(x)  # take care of the processed request
                    requests_list.remove(x)  # remove processed request
                    # check if finish the whole request list
                    if len(requests_list) == 0:
                        seek_time = abs(max_request - cur_position)
                        cur_position = x  # update current position
            temp1_time = 199 - cur_position
            # seek back up from 200 to min if not finish requests
            if len(requests_list) > 0:
                for y in range(200, min_request - 1, -1):
                    if y in requests_list:
                        schedule.append(y)  # take care of the processed request
                        requests_list.remove(y)  # remove processed request
                temp2_time = abs(199 - y)
                seek_time = temp1_time + temp2_time
                cur_position = y  # update current position
        # head move to the left first
        else:
            # print "left"
            for x in range(position, -1, -1):
                if x in requests_list:
                    schedule.append(x)
                    requests_list.remove(x)
                    # check if finish the whole request
                    if len(requests_list) == 0:
                        seek_time = abs(cur_position - min_request)
                        cur_position = x  # update current position
            temp1_time = abs(0 - cur_position)
            # seek back up from 0 to max if not finish request
            if len(requests_list) > 0:
                for y in range(0, max_request + 1):
                    if y in requests_list:
                        schedule.append(y)
                        requests_list.remove(y)
                temp2_time = abs(0 - max_request)
                seek_time = temp1_time + temp2_time
                cur_position = y  # update current position
        total_time = total_time + seek_time
    print schedule
    print total_time
    print schedule[-1], total_time


fscan()
