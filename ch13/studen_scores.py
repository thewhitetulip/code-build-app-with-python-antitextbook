input_file = open("data.csv", "r")
score = input_file.readlines()
score = [line.strip() for line in score]

heading = score[0].split(",")
score = score[1:]
total_subjects = len(heading)

marks = {}

for i in range(len(score)):
    sc = score[i].split(",")
    marks[sc[0]] = sc[1:]

# Find out the name of student who has score maximum marks in each subject

for name in marks.keys():
    