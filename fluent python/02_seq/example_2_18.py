
import bisect 

def grade(score, breakpoint = [60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoint, score)
    return grades[i]



print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])
