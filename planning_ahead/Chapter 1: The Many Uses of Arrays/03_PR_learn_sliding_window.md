
# ========== Learning the Sliding Window approach ==========

## Instructor Notes
1. Talk about the class of problems that are "find the longest sub-array that matches condition" or "find the number of sub-arrays that match condition"
2. Talk about the naive solutions that run in n^2 time (which is really bad!)
```python

for i in range(n):
    for j in range(i, n):
        # Do some logic here
        ...
```
3. Talk about the sliding window approach -- that is, have a loop that on each iteration moves the right pointer forward one index. Then checks the condition, and if the condition is violated then shrinks the left pointer until the condition is no longer violated.
4. Mention that it is important to pay attention to how you define your indices for the sub-array. If you use indices like they are treated in slice notation (start:end), then the window DOES NOT include the element at end, and the length of the array is `end - start`. If you define your indices such that the end element is included, then the length of your sub-array is calculated with `end - start + 1`, and you need to remember that when the array has zero elements, the start index will actually be past the end index. **Both ways are OK, but know which one you are using and be consistent within that problem to avoid confusing yourself.**
5. My personal experience is that if it is possible for your window to be length zero, then it is better to use slice notation rather than inclusive bounds, because this maintains the relationship `start <= end` for all possible sub-arrays, and this makes it easier to reason about. 
6. Do not, however, that the `pandas` library uses inclusive bounds for it's slice notation, which is different than the python language.

## Story Interlude
You come into work earlier than normal, feeling groggy. While standing in the office kitchen waiting for your coffee to brew, you overhear Franchesca and Alejandro fighting. You aren't trying to eavesdrop, but they are yelling so loud that you would have to plug your ears in order to not hear. You are clearly missing some context, but the argument seems to be about doing chores. This is clearly 

## Problem Context
Alejandro has just finished work on a project for Jay. Jay is worried that with the odd office hours everyone keeps, they might not always put in the full time hours they are getting paid for. But he doesn't want to mandate strict daily hours, because sometimes he wants people to work more than 8 hours in a day. So he had Alejandro put together a dashboard where he can monitor the average hours everyone works.

Alejandro wrote a function that takes a list of integers named `hours`, where `hours[i]` indicates the number of hours that a the employee worked on that day. The function returns an integer indicating the greatest number of contiguous work days that someone has gone where the average number of hours per day is less than x. If there is no such sequence of days, return 0.

Alejandro would like you to `Peer Review` his function before it gets merged to the codebase.

**Code:**
```python
def longest_work_period_under_hours(hours: list[int], x: int) -> int:
    """
    Return the length of the longest sequence of days with an average hours worked less than x.
    """
    # Note: I am using python slice-notation style indices for this function.
    
    left = 0
    right = 0
    hours_inside_window = 0
    answer = 0

    while right < len(hours):

        # Expand the window, and keep track of what the sum inside that window
        hours_inside_window += hours[right]
        right += 1

        # If the average is now more than the target x, we shrink the window
        # until either the average is below x or until the size of the window
        # is 0 elements (we don't want to divide by zero)
        number_of_days = right - left
        while number_of_days > 0 and hours_inside_window / number_of_days > x:
            
            # Shrink the window by one day
            hours_inside_window -= hours[left]
            left += 1
            number_of_days = right - left

        # The loop just above guarantees that at this point we meet the criteria
        # of interest: namely and average less than x. So we can update the answer
        # with the length of this sub array
        answer = max(answer, right - left)

    return answer
```


**Tests:**
```python

hours = [9, 7, 9, 9, 9]
x = 8
answer = 1
# Explanation: The largest subsequence of days with an average value less than 8
# is just the subsequence [7]. If we include one of the surrounding days, like [9, 7]
# or [7, 9] then the average across the two day is 8.
assert longest_work_period_under_hours(hours, x) == answer


hours = [8, 7, 6, 7, 8, 20, 18, 0, 0, 0, 8, 6, 8, 7, 8]
x = 7
answer = 8
# Explanation: In this case we have 3 weeks Jean Pierre's work. The first is fairly typical.
# He kicks off the second week with a two day cocaine bender, from which it takes him the
# rest of the week to recover. Then he is back to a typical person's schedule the week after
# that, but the average has tanked to the point where it never gets back above 7.
# So the longest subsequence with an average below 7 is [18, 0, 0, 0, 8, 6, 8, 7]

```