
# LC 2376 - Hard
def countSpecialNumbers(n: int) -> int:
    
    def _perm(n: int, k: int) -> int:
        """Calculates permutations (nPk): n * (n-1) * ... * (n-k+1)"""
        result = 1
        for _ in range(k):
            result *= n
            n -= 1
        return result
    
    s = str(n)
    L = len(s)
    total_special_numbers = 0

    if L > 1:
        total_special_numbers += 9
        current_length_combinations = 9
        available_digits = 9

        for i in range(2, L):
            current_length_combinations *= available_digits
            total_special_numbers += current_length_combinations
            available_digits -= 1

    
    used_digits = set()
    for i, char in enumerate(s):
        current_target_digit = int(char)

        start_digit = 1 if i == 0 else 0

        for d in range(start_digit, current_target_digit):
            if d not in used_digits:
                empty_slots = L - 1 - i
                available_digits = 9 - i
                total_special_numbers += _perm(available_digits, empty_slots)
                
            
        if current_target_digit in used_digits:
            break
        used_digits.add(current_target_digit)
    else:
        total_special_numbers += 1

    return total_special_numbers