from tkinter import *
from math import floor

# -------- CONSTANTS --------- #
BLUE, PINK, RED, YELLOW, WHITE, GREEN = "#1D2B53", "#7E2553", "#FF004D", "#FAEF5D", "white", "green"
FONT_COURIER, FONT_GEOMETOS, FONT_LEMON = "Courier", "Geometos", "Lemon/Milk"
WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN, SECONDS_IN_MINUTE = 25, 5, 20, 60

# Globals with non-constant values
reps = 1
timer_mechanism = None


# ---- TIMER RESET---- #
def reset_timer():
    """Resets the timer"""
    global reps, timer_mechanism
    reps = 1
    window.after_cancel(timer_mechanism)
    label.config(text="Timer", fg=WHITE)
    canvas.itemconfig(pomodoro_timer, text="00:00")
    checkbox_label.config(text="")


# ------ TIMER MECHANISM ------ #
def start_timer():
    """Starts the timer from work of 25 minutes and rest of 5 minutes"""
    work_seconds = WORK_MIN * SECONDS_IN_MINUTE
    rest_seconds = SHORT_BREAK_MIN * SECONDS_IN_MINUTE
    long_break_seconds = LONG_BREAK_MIN * SECONDS_IN_MINUTE

    # We'll check if reps is of work, rest or break, odd is "work", even is "rest/break"
    if reps in (1, 3, 5, 7):
        label.config(text="Work", fg=RED)
        count_down(work_seconds)
    elif reps in (2, 4, 6):
        label.config(text="Rest", fg=GREEN)
        count_down(rest_seconds)
    elif reps == 8:
        label.config(text="Break", fg=YELLOW)
        count_down(long_break_seconds)


# ------ COUNTDOWN MECHANISM -------- #
def count_down(counter_time):
    """Counter for the timer to keep track of time"""
    if counter_time >= 0:
        # We'll take quotient and remainder of time in seconds, quotient = minutes, while remainder = seconds
        counter_minutes, counter_seconds = divmod(counter_time, SECONDS_IN_MINUTE)
        # Makes sure that if time is below 10, i.e. 8, it'll show "00:08" not "0:8"
        counter_minutes = f"0{counter_minutes}" if counter_minutes < 10 else counter_minutes
        counter_seconds = f"0{counter_seconds}" if counter_seconds < 10 else counter_seconds

        canvas.itemconfig(pomodoro_timer, text=f"{counter_minutes}:{counter_seconds}")
        global timer_mechanism
        timer_mechanism = window.after(1000, count_down, counter_time - 1)
    else:
        # Everytime timer hits 00:00, reps increase, and a check-mark added for "work" reps
        global reps
        reps += 1
        if reps % 2 == 0:
            checkbox_label.config(text="✅" * int(reps/2))
        start_timer()


# ------- UI SETUP ---------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=180, pady=40, bg=BLUE)

label = Label(text="Timer", font=(FONT_GEOMETOS, 30, "bold"))
label.config(bg=BLUE, fg=WHITE, padx=20)
label.grid(column=1, row=0)

canvas = Canvas(width=250, height=274, bg=BLUE, highlightthickness=0)
# Adjust path to tomato.png to your local directory
tomato_bg_image = PhotoImage(file="tomato.png")
canvas.create_image(127, 127, image=tomato_bg_image)
pomodoro_timer = canvas.create_text(127, 145, text="00:00", fill=WHITE, font=(FONT_LEMON, 25, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", fg=WHITE, bg=RED, font=(FONT_COURIER, 10, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

checkbox_label = Label(bg=BLUE, fg=YELLOW)
checkbox_label.grid(column=1, row=2)

reset_button = Button(text="Reset", fg=WHITE, bg=RED, font=(FONT_COURIER, 10, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
