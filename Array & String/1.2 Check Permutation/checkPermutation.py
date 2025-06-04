def checkPermutation(s: str, t: str) -> bool:
    
    hashmap = {}

    for c in s:
        hashmap[c] = hashmap.get(c,0) + 1

    for c in t:
        if c not in hashmap:
            return False
        
        hashmap[c] -= 1

        if hashmap[c] == 0:
            del hashmap[c]
        
    return len(hashmap) == 0
    
def checkPermutation(s: str, t:str) -> bool:
    
    count = [0] * 128

    for c in s:
        count[ord(c)] += 1

    for c in t:
        count[ord(c)] -= 1

        if count[ord(c)] < 0:
            return False
    
    return all(value == 0 for value in count)
    
