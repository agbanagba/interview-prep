from typing import List    

def restoreIpAddresses(s: str) -> List[str]:
        
        def backtrack(idx, ip):

            if idx == len(s) and len(ip) == 4:
                result.append(".".join(ip))
                return 

            if len(ip) == 4:
                return

            for end_idx in range(idx + 1, min(idx + 4, len(s) + 1)):

                c_slice = s[idx:end_idx]

                # Determine validitiy of the c_slice
                # No leading zeros and between the range of 0 and 255. 
                # if not continue
                if len(c_slice) > 1 and c_slice[0] == "0":
                    continue
                
                ci_slice = int(c_slice)
                if not (0 <= ci_slice <= 255):
                    continue

                ip.append(c_slice)
                backtrack(end_idx, ip)
                ip.pop()


        result = []
        backtrack(0, [])
        return result