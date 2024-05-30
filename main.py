from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="{:02d}".format(0) + ":" + "{:02d}".format(0))
    timer_label.config(text="TIMER", fg=GREEN)
    rounds_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    if reps == 7:
        timer_label.config(text="Long Break", fg= RED)
        count_down(LONG_BREAK_MIN*60)
    elif reps % 2 == 0:
        timer_label.config(text="Work Time", fg=GREEN)
        count_down(WORK_MIN*60)
    else:
        timer_label.config(text="Short Break", fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
    rounds = math.ceil(reps / 2)
    rounds_label.config(text="✓" * rounds)
    reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    if count >= 0:
        timer = window.after(1000, count_down,count-1)
        count_min = math.floor(count / 60)
        count_sec = int(count % 60)
        canvas.itemconfig(timer_text, text= "{:02d}".format(count_min) + ":" + "{:02d}".format(count_sec))
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

#Timer label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=1, row=0)

#Tomato canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img= PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text= canvas.create_text(100,130, text="00:00", fill="white", font= (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#Start Button
start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

#Reset Button
reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

#Rounds label
rounds_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
rounds_label.grid(column=1, row=3)

window.mainloop()