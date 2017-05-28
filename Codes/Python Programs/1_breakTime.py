import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on ", time.ctime())
while(break_count < total_breaks):
    time.sleep(3600)  # in secs
    webbrowser.open("https://www.youtube.com/watch?v=ikUBr-7svb4")
    break_count += 1
