from tkinter import messagebox, Label, Button, Tk, END, filedialog, Text
from timer import Timer
import random
import time


countdown = None
start_time = 0
end_time = 0
r_start = [
    "It was up to her to investigate how the accident had really happened",
    "He had to find out what happened last night",
    "She wanted to find out what happened to her father back then",
    "After he heard the news, He hurried back",
    "They'd only been apart for a week and already he had a new lover hanging off his arm"
]

timer = 15


def is_writing(event):
    """cancels the running countdown, resets the timer by resetting the displayed text, calls function start_timer"""
    global countdown
    try:
        window.after_cancel(countdown)
        timer.config(text="5 secs")
        start_timer(5)

    except ValueError:
        messagebox.showinfo(title="Wait!", message='You forgot to hit the start button')


def generate_prompt():
    global start_time
    start_timer(5)
    random_choice = random.choice(r_start)
    label["text"] = random_choice
    text_input.focus()
    start_time = time.time()


def end_app():
    text_input.delete(0, END)


def start_timer(count):
    global countdown
    if count >= 0:
        timer.config(text=f"{count} secs")
        countdown = window.after(1000, start_timer, count - 1)
    else:
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
            return
        story = text_input.get()
        f.write(story)
        f.close()
        end_app()
        calculate_time()



def calculate_time():
    global start_time, end_time
    end_time = time.time()
    run_time = round((end_time - start_time) / 60)
    messagebox.showinfo(title="Complete!", message=f"You were writing for {run_time} min")
    start_time = 0
    end_time = 0


window = Tk()
window.title("Writer Block Exercise")
window.minsize(width=500, height=200)
window.config(width=51, height=15, padx=25, pady=25)

label = Label(text='Welcome to the Random Prompt Generator!', font=("Helvetica", 20))
label.grid(column=1, row=0, columnspan=2)

text_input = Text(width=51, font=("Helvetica", 20))
text_input.grid(column=1, row=1, columnspan=3)

button = Button(text='Get Prompt', command=generate_prompt)
button.grid(column=1, row=3, columnspan=3)


timer = Timer()

text_input.bind("<Key>", is_writing)

window.mainloop()
