

def generateAbbreviations(word: str) -> list[str]:

    result = []

    def backtrack(idx, path, count):
        
        if idx == len(word):
            if count > 0:
                path.append(str(count))

            result.append("".join(path))
            
            if count > 0:
                path.pop()

            return 

        # we abbreviate the current letter. 
        # this means we increment count and don't do anything. 
        # something will be done when we hit the constraints 
        backtrack(idx + 1, path, count + 1)

        # choice 2. we don't abbreviate(convert into a number)
        # we instead use it i.e, we append it to the path
        # but we first need to append count

        items_added = 0
        if count > 0:
            path.append(str(count))
            item_added += 1

        path.append(word[idx])
        item_added += 1
        
        backtrack(idx + 1, path, 0)

        for _ in range(items_added):
            path.pop()

    backtrack(0, [], 0)
    return result