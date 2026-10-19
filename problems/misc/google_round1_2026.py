import random
from collections import defaultdict

class ExperimentGroup:

    def __init__(self):
        self.groups = {}

        # Cummulative sum maps 
        self.cummulative_sum = []

    def add_slot(self, experiment_id, variant_name):

        groups = self.groups

        if experiment_id not in groups:
            groups[experiment_id] = {"slots": defaultdict(int), "total_slots": 0}

        slots = groups[experiment_id]['slots']
        slots[variant_name] += 1
        groups[experiment_id]["total_slots"] += 1
        

    # O(N) where n is variant_names. Building the cummulative weights looks through all values of N
    # We could optimise this into O(1) by keeping the cummulative sum and updating it on add_slot
    def assign_and_consume(self, experiment_id):
        
        if experiment_id not in self.groups:
            return None
        
        slots = self.groups[experiment_id]["slots"]
        if not slots:
            return None
        
        # O(N) space to keep keys + O(N) space to keep cumm_sum on each call. 
        keys = list(slots.keys())

        # build cummulative sum of items
        total = 0
        cumm_sum = []
        for weight in slots.values():
            total += weight
            cumm_sum.append(total)

        target = random.random() * total
        for i, boundary in enumerate(cumm_sum):
            if target < boundary:
                item = keys[i]
                slots[item] -= 1
                return item
            
        return None # Ideally, we will not reach here because we are generating a random number based on total. 

if __name__ == "__main__":

    group = ExperimentGroup()

    group.add_slot(1, "blue")
    group.add_slot(1, "blue")
    group.add_slot(1, "red")

    print(group.assign_and_consume(1))
    print(group.assign_and_consume(1))