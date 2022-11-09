"""
INPUT

ask the user for their name

ask the user for the names(s) of the file(s) they want sent to the printer.

randomly give the file name an extension (pdf, doc, png, gif, jpg)

DISPLAY

PRETEND to have items print out in order they were sent to the printer (see image above).  Disregard pages, size.

Get the time from the date/time function for displaying when it was sent.

display the printer queue to the user after all the items have been sent.

PRINTER FAILURES:

Have a random number generator between 1-10.  If the number is between 1-3, the print job failed.

When an item fails, ask the user if they want to WAIT or REMOVE the item

if they wait, have a random number generator that decides if the print job goes through( random number between 1-10, with a 50% chance)

If it fails again, ask the user if they want to WAIT or REMOVE (repeat the process of the random number)

PRINTER SUCCESSES:

Time delay between each successful printing (the time duration is your choice, but it shouldn't be long)

If the print job is successful, remove it from the list.

Display the list as it goes

DISPLAY:

STATUS: always show the status of each print job.

Once the queue is empty, tell the user the print queue is empty and display it

start the process over again ask for items to be printed.

What you will need to use :

popleft(0)

pop()

append

functions
"""

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

                print(fail_again)

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
