# This is a python mini project to remind a user that "it's time to study!" 
# Once a user runs the program, it keeps tracking time and opens the browser to play learning videos.

import webbrowser
import time

total_lessons = 3 # number of lessons thoughtout the day
lessons_count = 0 # initialize count

# This function picks a lesson for a user
def choose_lesson(lessons_count):
    link1 = "https://www.youtube.com/watch?v=ODgLHqCAJTw&list=PLAwxTw4SYaPmtf5v3hefG5seVynUtV9T8"
    link2 = "https://www.youtube.com/watch?v=33F1s0iDlEk&index=2&list=PLAwxTw4SYaPmtf5v3hefG5seVynUtV9T8"
    link3 = "https://www.youtube.com/watch?v=69ts0oBmnaE&list=PLAwxTw4SYaPmtf5v3hefG5seVynUtV9T8&index=3"

    if lessons_count == 0:
        return link1
    elif lessons_count == 1:
        return link2
    elif lessons_count == 2:
        return link3


print("This program started on" + time.ctime())
while(lessons_count < total_lessons):
    time.sleep(10)
    link = choose_lesson(lessons_count)
    webbrowser.open(link)
    lessons_count = lessons_count + 1

