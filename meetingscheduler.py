# Meeting scheduler

def getMinRooms(meetingTimings):
    # Write your code here
    numberofmeetings = len(meetingTimings)
    meetingTimings.sort()
    print(meetingTimings)
    current = []
   
    if len(meetingTimings) != 0:
        current.append(meetingTimings[0][1])
        count  = 1
    
  
    for i in range(1,numberofmeetings):
        if meetingTimings[i][0] < min(current):
            current.append(meetingTimings[i][1])
            count +=1
        else:
            current.remove(min(current))
            current.append(meetingTimings[i][1])
    return count
        

meetingTimings = [[2,8],[3,9],[5,11],[3,4],[11,15],[8,20]]
print(getMinRooms(meetingTimings))