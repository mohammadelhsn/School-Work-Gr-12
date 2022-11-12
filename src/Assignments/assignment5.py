#############################################################################
#Author: Mohammad El-Hassan
#Description: Assignemnt #5
#Date Created: 11/12/2022
#Date Modified: 11/12/2022
#############################################################################

import random
import datetime
import time
import collections

FILE_EXTENSIONS = ["pdf", "docx", "png", "gif", "jpg", "txt"]


def printer_queue(queue):
    # 14
    document = f"___Document___"
    # 12
    status = f"___Status___"
    # 11
    owner = "___Owner___"
    # 15
    submitted = "___Submitted___"

    print(f"{document}{status}{owner}{submitted}")

    for file in queue:
        name = f"{file['filename']}" + " " * (len(document) - len(file["filename"]) + 3)
        stat = f"{file['status']}" + " " * (len(status) - len(file["status"]))
        ow = f"{file['owner']}" + " " * (len(owner) - len(file["owner"]))
        sub = f"{file['submitted']}" + " " * (len(submitted) - len(file["submitted"]))

        print(f"{name}{stat}{ow}{sub}")
        time.sleep(0.5)


def failure():
    num = random.randint(1, 10)
    fail = [1, 2, 3]

    if num in fail:
        return True
    else:
        return False


def wait():
    num = random.randint(1, 10)

    if num >= 5:
        return True
    else:
        return False


while True:
    name = input("What is your full name?")

    num_of_files = int(input("How many files would you like to print? "))

    queue = collections.deque([])

    for i in range(num_of_files):
        extension = random.choice(FILE_EXTENSIONS)
        filename = input("What is the name of the file? ")
        queue.append(
            {
                "filename": f"{filename}.{extension}",
                "status": "waiting",
                "owner": name,
                "submitted": str(datetime.datetime.today()),
            }
        )

    printer_queue(queue)
    completed = []
    print(f"🖨️ | Proceeding...")
    index = -1
    for i in range(len(queue)):
        file = queue[index + 1]
        file["status"] = "printing"
        printer_queue(queue)
        print(f"Attempting to print {file['filename']}")

        fail = failure()

        while fail == True:
            print(f"❌ | The print failed!")
            action = int(input("What would you like to do? 1) Wait 2) Remove"))

            if action == 1:
                fail_again = wait()

                if fail_again == True:
                    continue
                else:
                    fail = False
                    break
            else:
                a = queue.popleft()
                a["status"] = "removed"
                completed.append(a)
                print(f"✅ | Removed {file['filename']}")
                break

        if fail == False:
            print(f"✅ | Printed {file['filename']}")
            a = queue.popleft()
            a["status"] = "printed"
            completed.append(a)
            continue

    for a in completed:
        print(f"✅ | {a['filename']}: {a['status']}")
