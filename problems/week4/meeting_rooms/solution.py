def can_attend_meetings(intervals):
    if not intervals:
        return True

    intervals.sort(key=lambda x: x[0])  # This is already O(nlogn) best case
    for idx in range(1, len(intervals)):
        interval = intervals[idx]
        if interval[0] < intervals[idx - 1][1]:
            return False

    return True


def min_meeting_rooms(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])

    # Creating a meeting room for the first meeting and putting the first end time
    rooms = [intervals[0][1]]

    for interval in intervals[1:]:
        free_slot_idx = -1
        for room_idx, room_end_time in enumerate(rooms):
            if interval[0] >= room_end_time:
                free_slot_idx = room_idx
                break

        if free_slot_idx != -1:
            rooms[free_slot_idx] = interval[1]
        else:
            rooms.append(interval[1])

    return len(rooms)


if __name__ == '__main__':
    interval1 = [[0, 30], [5, 10], [15, 20]]
    interval2 = [[7, 10], [2, 4]]
    interval3 = [[4, 9], [4, 17], [9, 10]]
    # print(can_attend_meetings(interval1))
    print(min_meeting_rooms(interval1))
