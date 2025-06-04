def isUnique(s: str) -> bool:

    hashset = set()

    for c in s:

        if c in hashset:
            return False
        
        hashset.add(c)
        
    return True


def isUnique(s: str) -> bool:

    checker = 0

    for c in s:

        bit_position = 1 << (ord(c) - ord('a'))

        if checker & bit_position:
            return False
        
        checker |= bit_position
    
    return True