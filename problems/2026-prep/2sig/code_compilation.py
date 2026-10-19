# Code Compilation
# There is a group of codebases that need to be compiled, with the compile time and dependencies provided.
# The system allows unlimited parallelism, meaning any number of codebases can be built at the same time as long as their dependencies are satisfied.

# img

# Example Input:

# codebase2time = {"A":1, "B":3, "C":2, "D":2, "E":4}  
# dependency = {  
#   "B": {"A"},  
#   "C": {"A"},  
#   "D": {"B", "C"},  
#   "E": {"A", "C"}  
# }  
# For example, in this case, B and C can be compiled simultaneously. The order of codebases within the same level of parallel compilation does not matter. In other words, in the example below, the order of the letters on the same line is flexible. The task was to generate a build schedule that minimizes the total build completion time. The output was required to be a sequence of time slices. Each time slice is represented as a string in the format:

# <execution_time>,<codebase1>,<codebase2>,...
# This indicates that the listed codebases were built concurrently for the given duration. The exact ordering of codebases within a time slice did not matter, but the execution times and grouping had to reflect a valid and optimal schedule.

# Key constraints and expectations:

# A codebase can only start once all its dependencies are fully built.
# Once started, a codebase continues building until completion, but its execution may span multiple time slices.
# The scheduler should always run all currently-available builds in parallel.

from collections import defaultdict

import heapq

# Time complexity - O(VlogV + E) where V is the number of codebases and E is total number of dependencies. 
# Space complexity - O(V + E)
def get_build_schedule(codebase_time, dependency):

    # Phase 1: Setup adjacency list and in-degree map
    # unlocks is like a reverse dependency list for each codebase.
    unlocks = defaultdict(list)
    wait_count = {cb: 0 for cb in codebase_time} # start everyone at 0

    for dependent, prerequisites in dependency.items():
        wait_count[dependent] += len(prerequisites)
        for prereq in prerequisites:
            unlocks[prereq].append(dependent)

    
    # Phase 2: Initialise timers and state
    current_time = 0
    event_calendar = [] # min-heap storing tuples of (completion_time, codebase_id)

    # Kickoff: Add all tasks that have absolutely zero dependencies
    for cb, count in wait_count.items():
        if count == 0:
            heapq.heappush(event_calendar, (current_time + codebase_time[cb], cb))

    schedule_output = []

    # Phase 3: Simulation Loop
    while event_calendar:
        next_event_time = event_calendar[0][0]

        if next_event_time > current_time:
            duration = next_event_time - current_time

            # we don't have to sort the roster here but that's fine. Output will be "A,B"
            running_tasks = ",".join([task[1] for task in event_calendar])
            schedule_output.append(f"{duration},{running_tasks}")

            current_time = next_event_time

            # This loop needs to be looked at 
            while event_calendar and event_calendar[0][0] == current_time:
                _, finished_cb = heapq.heappop(event_calendar)

                for dependent in unlocks[finished_cb]:
                    wait_count[dependent] -= 1

                    if wait_count[dependent] == 0:
                        heapq.heappush(event_calendar, (current_time + codebase_time[dependent], dependent))


    return schedule_output



if __name__ == "__main__":

    times = {
        "A": 1,
        'B': 2, "C": 2, "D": 2, "E": 4
    }
    dependency = {
        "B": {"A"},
        "C": {"A"},
        "D": {"B", "C"},
        "E": {"A", "C"}
    }

    print(get_build_schedule(times, dependency))