# ========== Longest listen with at most k skips ==========


## Problem Context
Augment'd recently rolled out a new playlist feature. Fans can listen to an automatically generated playlist of songs based on the musicians they have followed. Jay has decided that he wants to measure the success of this feature with a key performance metric of "most songs listened to with at most some number of skips." He hasn't yet decided what "some number" should be, though.

You are tasked with writing a function that accepts a list of binary values named `statuses`. The value of `statuses[i]` will be 1 if the user finished the track, and 0 if the user pressed skip for the track. Your function should return the length of the longest array of tracks the user listened to that contains at most `k` skips. Skipped tracks still count toward the length of the array.

**Setup:**
```python
def longest_array(statuses: list[bool], k: int) -> int:
    pass
```

**Tests:**
```python
statuses = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
answer = 6
assert longest_array(statuses, k) == answer
# [1,1,1,0,0,0,1,1,1,1,0]
#            -----------


statuses = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
answer = 10
assert longest_array(statuses, k) == answer
# [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
#      -------------------
```

