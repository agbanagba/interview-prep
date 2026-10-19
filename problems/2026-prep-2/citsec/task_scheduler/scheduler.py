from typing import List

# Implement a round robin task scheduler

# There is LC 621 - Task scheduler. 
def leastInterval(tasks: List[str], n: int) -> int:
    pass


# Another variant is to create a task scheduler that allocate tasks to executors in 
# a round robin manner.

class RoundRobinScheduler:
    def __init__(self, tasks):
        self.tasks = tasks
        self.index = 0

    def get_next_task(self):
        if not self.tasks:
            return None

        task = self.tasks[self.index]
        self.index = (self.index + 1) % len(self.tasks)
        return task