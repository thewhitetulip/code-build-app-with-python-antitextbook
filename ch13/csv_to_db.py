## Converts data.csv to data.sql
# name,science,math,history
# tony,12,12,12
# antony,13,13,13
# bantony,14,14,14

# insert into student(name, science, math, history) values(line[0], line[1], line[2], line[3])


file_name = "data.csv"
input_file = open(file_name, "r")
output_file = open("data.sql", "w")

csv_lines = input_file.readlines()
csv_lines = [line.strip() for line in csv_lines]

INSRT_STMT = 'INSERT INTO STUDENT(NAME, SCIENCE, MATH, HISTORY) VALUES('

inserts = []

for line in csv_lines[1:]:
    iline = line.split(",")
    insert = INSRT_STMT + '"' + iline[0] + '"'
    for i in iline[1:]:
        insert += ","
        insert += i
    insert+=");\n"
    inserts.append(insert)

output_file.writelines(inserts)
output_file.close()