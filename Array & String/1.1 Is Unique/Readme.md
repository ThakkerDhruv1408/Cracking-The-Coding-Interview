### 1.1 Problem Statement 
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?

### Problem Understanding
The task is to check if a given string contains all unique characters, meaning no character repeats. For example, "abcde" has all unique characters, but "abcda" does not because 'a' appears twice. The second part of the question asks for a solution without using additional data structures, which adds a constraint to optimize for space.

Let’s break it down and solve it step-by-step.

---

### Approach 1: Using a Hash Set (With Additional Data Structure)
Let me start with the most intuitive approach using a hash set, which provides an efficient way to track characters we’ve seen.

1. **Idea**: Iterate through each character in the string and use a hash set to check if we’ve encountered it before. If we find a character already in the set, the string does not have all unique characters. If we complete the iteration without finding duplicates, all characters are unique.
2. **Time Complexity**: O(n), where n is the length of the string, as we traverse the string once.
3. **Space Complexity**: O(k), where k is the size of the character set (e.g., 128 for ASCII, 256 for extended ASCII).

Here’s how I’d code this in Python:

```python
def is_unique_with_set(s: str) -> bool:
    # Create a hash set to store characters
    char_set = set()
    
    # Iterate through each character
    for char in s:
        # If character is already in set, return False
        if char in char_set:
            return False
        # Add character to set
        char_set.add(char)
    
    return True
```

**Explanation**:
- I use a Python `set` to store characters. The `in` operation for a set is O(1).
- For each character, I check if it’s in the set. If it is, I return `False` since we’ve found a duplicate.
- If I finish the loop, I return `True` as no duplicates were found.
- This approach is efficient and straightforward, but it uses O(k) extra space for the set.

---

### Approach 2: Without Additional Data Structures
Now, let’s address the constraint of not using additional data structures. This is trickier because we can’t use a set or array to track seen characters. Let’s explore a few options:

1. **Sorting Approach**:
   - **Idea**: Sort the string and check adjacent characters for duplicates. If any adjacent characters are the same, the string has duplicates.
   - **Time Complexity**: O(n log n) due to sorting, where n is the string length.
   - **Space Complexity**: O(1) if we assume sorting modifies the string in-place (though Python’s sorting creates a new list, we’ll discuss this).
   - **Caveat**: In Python, strings are immutable, so sorting requires creating a new list, which technically uses O(n) space. To strictly adhere to “no additional data structures,” we’d need a language where in-place sorting is possible, but let’s code it in Python for clarity and note this.

2. **Brute Force Approach**:
   - **Idea**: For each character, compare it with every subsequent character to check for duplicates.
   - **Time Complexity**: O(n²), as we perform a nested loop.
   - **Space Complexity**: O(1), as we only use a few variables.
   - **Drawback**: This is less efficient but meets the no-extra-space requirement.

3. **Bit Vector Approach** (for limited character set, e.g., lowercase letters a-z):
   - **Idea**: Use a single integer as a bit vector to mark seen characters (e.g., for lowercase letters, we need 26 bits). This technically uses O(1) space (a fixed-size integer) but assumes a limited character set.
   - **Time Complexity**: O(n).
   - **Space Complexity**: O(1).

Since the question doesn’t specify the character set, let’s assume ASCII for generality. The brute force approach is the most universally applicable without extra space, but I’ll also discuss the bit vector approach for optimization if we assume lowercase letters. Let’s code both and explain trade-offs.

#### Brute Force Solution (No Extra Data Structures)
```python
def is_unique_brute_force(s: str) -> bool:
    # Compare each character with all subsequent characters
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True
```

**Explanation**:
- I use two nested loops to compare each character with all characters after it.
- If any pair matches, I return `False`.
- If no matches are found, I return `True`.
- **Pros**: Truly O(1) space, as we only use loop variables.
- **Cons**: O(n²) time complexity, which is inefficient for large strings.

#### Bit Vector Solution (Assuming Lowercase Letters a-z)
If we assume the string contains only lowercase letters (a-z), we can optimize using a bit vector:

```python
def is_unique_bit_vector(s: str) -> bool:
    # Assuming lowercase letters a-z
    checker = 0  # Bit vector
    
    for char in s:
        # Map character to bit position (e.g., 'a' -> 0, 'b' -> 1)
        bit_position = 1 << (ord(char) - ord('a'))
        # If bit is already set, char is a duplicate
        if checker & bit_position:
            return False
        # Set the bit for this character
        checker |= bit_position
    
    return True
```

**Explanation**:
- I use an integer `checker` as a 32-bit vector (since we only need 26 bits for a-z).
- For each character, I compute its bit position (e.g., ‘a’ maps to bit 0, ‘b’ to bit 1).
- I check if the bit is set using `checker & bit_position`. If set, the character is a duplicate.
- If not, I set the bit using `checker |= bit_position`.
- **Pros**: O(n) time and O(1) space (fixed-size integer).
- **Cons**: Only works for a limited character set (e.g., a-z). If the string has other characters, we’d need a larger bit vector or a different approach.

#### Sorting Solution
Here’s the sorting-based approach, noting the Python caveat:

```python
def is_unique_sorting(s: str) -> bool:
    # Convert string to list for sorting (Python strings are immutable)
    sorted_s = sorted(s)
    # Check adjacent characters
    for i in range(len(sorted_s) - 1):
        if sorted_s[i] == sorted_s[i + 1]:
            return False
    return True
```

**Explanation**:
- I sort the string, which groups duplicate characters together.
- I check adjacent characters for equality.
- **Pros**: O(n log n) time, conceptually simple.
- **Cons**: In Python, `sorted(s)` creates a new list, using O(n) space. In languages like C++ with mutable strings, we could achieve O(1) space with in-place sorting.

---

### Optimization and Trade-Offs
Let’s summarize and choose the best approach:

1. **Hash Set**: O(n) time, O(k) space. Fastest and most general, but uses extra space.
2. **Brute Force**: O(n²) time, O(1) space. Meets the no-extra-space requirement but is slow.
3. **Bit Vector**: O(n) time, O(1) space, but only works for a limited character set (e.g., a-z).
4. **Sorting**: O(n log n) time, O(1) space in theory (but O(n) in Python due to immutability).

For the **no extra data structure** constraint, the brute force approach is the safest as it universally works with O(1) space. However, if the interviewer confirms the input is limited to lowercase letters, the bit vector approach is optimal with O(n) time and O(1) space. Since the question doesn’t specify the character set, I’d lean toward the brute force solution for correctness but mention the bit vector as an optimization if applicable.

---

### Final Solution
Let’s present the brute force solution as the primary answer for the no-extra-space constraint, with a note on the bit vector optimization:

```python
def is_unique(s: str) -> bool:
    # Brute force: O(n^2) time, O(1) space
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True
```

**Note**: If the input is guaranteed to be lowercase letters (a-z), we can optimize to O(n) time and O(1) space using a bit vector:

```python
def is_unique_optimized(s: str) -> bool:
    # Assuming lowercase letters a-z
    checker = 0
    for char in s:
        bit_position = 1 << (ord(char) - ord('a'))
        if checker & bit_position:
            return False
        checker |= bit_position
    return True
```

---

### Edge Cases and Testing
Before finalizing, let’s consider edge cases:
- **Empty string**: Should return `True` (no duplicates).
- **Single character**: Should return `True`.
- **All same characters**: Should return `False` (e.g., "aaa").
- **Case sensitivity**: Assume case matters (e.g., 'A' and 'a' are different unless specified).
- **Non-lowercase characters** (for bit vector): We’d need to validate input or revert to brute force.

The brute force solution handles all edge cases. For the bit vector, we’d need to add input validation:

```python
def is_unique_optimized_with_validation(s: str) -> bool:
    # Validate input is lowercase a-z
    for char in s:
        if not char.islower() or ord(char) < ord('a') or ord(char) > ord('z'):
            raise ValueError("String must contain only lowercase a-z")
    
    checker = 0
    for char in s:
        bit_position = 1 << (ord(char) - ord('a'))
        if checker & bit_position:
            return False
        checker |= bit_position
    return True
```