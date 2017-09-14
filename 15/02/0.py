import bisect
breakpoints = [60, 70, 80, 90]
grades = 'FDCBA'
scores = [33, 99, 77, 70, 89, 90, 100]
def grade(score, breakpoints=breakpoints, grades=grades):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

print('breakpoints:', breakpoints)
print('grades:', grades)
print('scores:', scores)
print([grade(score) for score in scores])
