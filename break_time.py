import time
import webbrowser

total_breaks = 3
break_count = 0

print("Inicio " + time.ctime())

while(break_count < total_breaks):
    time.sleep(2)
    webbrowser.open("https://www.youtube.com/watch?v=rk6NNJJb1v8&index=4&list=WL&t=1845s")
    break_count = break_count + 1
