# Enunciado

"""
Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College.
One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
Formula used: Average = Sum of Distinct Heights/Total Numbers of Distinct Heights
"""

# Solución

def average(array):
    heights = set(array)
    average_heights = sum(heights)/len(heights)
    return average_heights
print(average([161, 182, 161, 154, 176, 170, 167, 171, 170, 174]))