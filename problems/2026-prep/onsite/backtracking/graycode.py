from typing import List    

def grayCode(n: int) -> List[int]:
        
        def backtrack(bit):

            if len(bit) == n:
                # Before we append to result, we have to 
                # make sure that bit diff between this and prev bit is 1
                current_bit = "".join(bit)
                prev_bit = result[-1] if result else None

                if prev_bit and (int(current_bit, 2) ^ int(prev_bit, 2)).bit_count() != 1:
                    return 
                
                result.append(current_bit)
                return

            for b in ["0", "1"]:

                bit.append(b)
                backtrack(bit)
                bit.pop()


        result = []
        backtrack([])
        return result