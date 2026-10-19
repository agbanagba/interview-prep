

def isAdditiveNumber(self, num: str) -> bool:
    
    def backtrack(idx: int, path: list[int]) -> bool:

        if idx == len(num):
            return len(path) >= 3

        for end_idx in range(idx + 1, len(num) + 1):
            slice_str = num[idx: end_idx]
            if len(slice_str) > 1 and slice_str[0] == '0':
                break

            current_num = int(slice_str)


            if len(path) >= 2:
                expected_sum = path[-1] + path[-2]

                if current_num != expected_sum:
                    continue

            path.append(current_num)
            if backtrack(idx + 1, path):
                return True

            path.pop()


        return False
    
    return backtrack(0, [])