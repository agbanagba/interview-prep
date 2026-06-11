

# First solution: Reuse meeting rooms
# We assign a meeting room to first meeting and for each subsequent 
# meeting, we check if the start time > end time of any used room and Reuse

# In the worst case, this is O(n2) because of the inner loop. 

def min_meeting_rooms(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])

    # We only track end time
    rooms = [intervals[0][1]] # Put the first meeting end time

    for interval in intervals[1:]:
        free_room_slot = -1
        for idx, end_time in enumerate(rooms):
            if interval[0] >= end_time:
                free_room_slot = idx
                break

        if free_room_slot != -1:
            rooms[free_room_slot] = interval[1]
        else:
            rooms.append(interval[1])
        
    return len(rooms)


# This solution here uses the sweep line technique. 
def min_meeting_rooms_sweep_line(intervals) -> int:
    if not intervals:
        return 0

    events = []
    for start, end in intervals:
        events.append((start, +1))
        events.append((end, -1))

    events.sort()

    rooms = 0
    active_rooms = 0
    for t, delta in events:
        active_rooms += delta
        rooms = max(rooms, active_rooms)

    return rooms