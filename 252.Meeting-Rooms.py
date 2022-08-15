# Given an array of meeting time intervals where 
# intervals[i] = [starti, endi], determine if a 
# person could attend all meetings.

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: true

def canAttendMeetings(intervals):
    sorted_intervals = sorted(intervals)
    for i in range(len(sorted_intervals) - 1):
        if sorted_intervals[i][1] > sorted_intervals[i+1][0]:
            return False
    return True 

print(canAttendMeetings([[0,30],[5,10],[15,20]]))
print(canAttendMeetings([[7,10],[2,4]]))
