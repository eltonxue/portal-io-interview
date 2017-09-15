'''
Created on Sep 15, 2017

@author: eltonxue
'''
# Potential conflict cases:
# Start - [100, 250], End - [50, 300]
# Start - [100, 250], End - [150, 300]
# Start - [100, 250], End - [50, 150]
# Start - [100, 250], End - [150, 200]

# Converted all times into Unix timestamps

# Added events:
# - "ICS 45C midterm exam" -> March 11th, 2017 -> 12:00pm - 2:00pm  -> CONFLICT
# - "Lunch with Professor Pattis" - March 11th -> 1:00pm - 1:30pm -> CONFLICT
# - "Flight to China" -> March 14th, 2017 -> 1:00am - 1:00pm
# - "Dedicated studying" -> February 23rd, 2017 -> 4:00pm - 7:00pm -> CONFLICT

events = [["Interview at The Portal", 1487862000, 1487867400], # February 23rd, 2017 -> 3:00pm - 4:30pm - CONFLICT
          ["Lunch with Cindy", 1488024000, 1488027600], # February 25rd, 2017 -> 12:00pm - 1:00pm
          ["Dinner with John", 1487955600, 1487957400], # February 24rd, 2017 -> 5:00pm - 5:30pm -> CONFLICT
          ["Conference", 1487934000, 1487957400], # February 24rd, 2017 -> 11:00am - 5:30pm -> CONFLICT
          ["ICS 45C midterm exam", 1489233600, 1489240800],
          ["Lunch with Professor Pattis", 1489237200, 1489239000],
          ["Flight to China", 1489453200, 1489496400],
          ["Dedicated studying", 1487865600, 1487876400]]


def eventConflicts(events):
    
    sortedEvents = sorted(events, key = lambda x: x[1]) # Sort events based on start times
    
    conflicts = set()
    
    endTime = 0
    currEndTime = 0
    
    for i in range(len(sortedEvents) - 1):
        currEndTime = sortedEvents[i][2]
        
        if (currEndTime > endTime): # replace old end time if current end time is greater
            endTime = currEndTime
        
        if (sortedEvents[i + 1][1] < endTime): # Compare next event start time with current end time
            conflicts.add(sortedEvents[i][0])
            conflicts.add(sortedEvents[i + 1][0])
    
    return list(conflicts)

correctConflicts = ["Interview at The Portal", "Dinner with John", "Conference", "ICS 45C midterm exam", "Lunch with Professor Pattis", "Dedicating studying"]
myConflicts = eventConflicts(events)

# Sorted for easier read in console
print("Should be:")
print(sorted(correctConflicts))
print("My answer:")
print(sorted(myConflicts))

