first_file = open("file.txt")
second_file = open("file2.txt")

first_lines = first_file.readlines()
second_lines = second_file.readlines()

first_lines = [line.strip() for line in first_lines]
second_lines = [line.strip() for line in second_lines] 

final_lines = {}

for line in first_lines:
    if line not in final_lines.keys():
        final_lines[line] = 0
    else:
        final_lines+=1

for line in second_lines:
    if line not in final_lines.keys():
        final_lines[line] = 0
    else:
        final_lines[line]+=1

lines = "\n".join(list(final_lines.keys()))

file = open("output.txt", "w")
file.write(lines+"\n")
file.close()