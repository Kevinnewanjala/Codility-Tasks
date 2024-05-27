def solution(A):
    # Get the length of the input array
    n = len(A)
    
    # If the length is less than 2, there is no increasing subsequence
    if n < 2:
        return n
    
    # Initialize variables for the left and right pointers
    left = 0
    right = 1
    
    # Initialize the maximum length of the increasing subsequence
    max_length = 2
    
    # Iterate through the array
    while right < n:
        # If the current element is less than the previous element, it marks the end of an increasing subsequence
        if A[right] < A[right - 1]:
            # Iterate from the left pointer to the right pointer to find the maximum length of the subsequence
            while left < right and A[left] > A[left + 1]:
                left += 1
            # Update the maximum length if the current subsequence is longer
            max_length = max(max_length, right - left + 1)
            # Reset the left pointer to the right pointer
            left = right
        # Move the right pointer to the next element
        right += 1
    
    # Handle the case where the last element is greater than the second-to-last element
    while left < n - 1 and A[left] > A[left + 1]:
        left += 1
    # Update the maximum length if the current subsequence is longer
    max_length = max(max_length, n - left)
    
    # Return the maximum length of the increasing subsequence
    return max_length

# Test the function with two examples
A = [1, 2]
print(solution(A))  # Output: 2
A = [2, 3, 3, 2, 2, 2, 1]
print(solution(A))  # Output: 4