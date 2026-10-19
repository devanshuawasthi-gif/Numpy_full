import numpy as np

names = np.array(['Aman', 'Riya', 'Karan', 'Neha', 'Zoya'])
marks = np.array([78, 92, 35, 88, 74])

print('Names:', names)
print('Marks:', marks)
print('Total:', np.sum(marks))
print('Average:', np.mean(marks))
print('Highest mark:', np.max(marks))
print('Lowest mark:', np.min(marks))

top = np.argmax(marks)
print('Top student:', names[top], marks[top])

passed = marks >= 40
print('Passed:', names[passed])
print('Failed:', names[~passed])
print('Scored 75 or more:', names[marks >= 75])

# Add 5 bonus points, with maximum score 100
updated = np.minimum(marks + 5, 100)
print('After bonus:', updated)

# Rank from highest score to lowest
order = np.argsort(marks)[::-1]
print('Ranking:')
for i in order:
    print(names[i], marks[i])