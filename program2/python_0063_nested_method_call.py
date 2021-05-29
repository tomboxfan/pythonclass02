animals = ['tiger', 'elephant', 'snake', 'shark']


# IMPORTANCE !!! ----------------------------
# Python runs code from top line to bottom line.
# In the same line, python runs from left to right.
# Here python notice, it needs to append something at the end of the animals list
# But Python tries figuring out what it should append, it notices it is another method call.
# So append method PAUSE first.
# Python will first call animals.pop(0), 'tiger' has been popped out, returned as the value to be appended
animals.append(animals.pop(0))
print(animals)
