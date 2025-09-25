"""
Given the names and grades for each student in a class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
There are 5 students in this class whose names and grades are assembled to build the following list:
python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
"""

if __name__ == '__main__':
    students = []
    scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scores.add(score)
    lower_score = sorted(scores)[1]
    names = []
    for name, score in students:
        if score == lower_score:
            names.append(name)
    for name in sorted(names):
        print(name)