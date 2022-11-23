import os
import time
import datetime

filePath = "src/Assignments/assignment3c.py"

created = os.path.getctime(filePath)
modified = os.path.getmtime(filePath)


print(time.ctime(created))
print(datetime.datetime.fromtimestamp(modified).strftime("%m/%d/%Y"))

file = open(filePath, "r")

lines = file.readlines()
line_created = lines[3]
line_modified = lines[4]
lines[
    4
] = f"# Date Modified: {datetime.datetime.fromtimestamp(modified).strftime('%m/%d/%Y')}\n"

file.close()

file = open(filePath, "w")

file.writelines(lines)

file.close()
