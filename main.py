import pyautogui
import tkinter as tk
from tkinter import Menu

x = 0
tab_out = bool
# Enable the failsafe
pyautogui.FAILSAFE = True


# The alt-tab setting
def alt_tab():
    global tab_out
    global x
    x = x + 1
    if x == 1:
        tab_out = True
    else:
        tab_out = False


# Function for the 'click' button
def click():
    click_amt = int(clicks_amount.get())
    wait = int(time_to_wait.get())
    wait = wait / 100
    if tab_out:
        pyautogui.hotkey("alt"+"tab")
    else:
        pass
    for i in range(0, click_amt):
        x_pos = int(x_to_click.get())
        y_pos = int(x_to_click.get())
        pyautogui.click(x_pos, y_pos)
        pyautogui.PAUSE = wait
        print(f"clicked {i + 1} time(s)")


# Style of the program
root = tk.Tk()

root.config(bg="black")

root.geometry("700x110")

root.resizable(False, False)

root.title("Simple Auto Clicker")

# root.attributes("-topmost", True)

# Menu Configuration
menubar = tk.Menu(root)

root.config(menu=menubar)

file_menu = Menu(menubar, tearoff=False)

file_menu.add_checkbutton(
    label="Alt-Tab after starting",
    command=alt_tab
)

file_menu.add_command(
    label="Exit",
    command=root.destroy,
)

menubar.add_cascade(label="Settings", menu=file_menu)

x_to_click = tk.Entry(root)
y_to_click = tk.Entry(root)
time_to_wait = tk.Entry(root)
clicks_amount = tk.Entry(root)
start_button = tk.Button(root, text="Click", command=click, width=12)

tk.Label(root, text="X Pos:", bg="black", fg="dark green").grid(row=0, column=1)
tk.Label(root, text="Y Pos:", bg="black", fg="dark green").grid(row=0, column=2)
tk.Label(root, text="Time between clicks (ms)", bg="black", fg="dark green").grid(row=2, column=1)
tk.Label(root, text="Amount to click:", bg="black", fg="dark green").grid(row=2, column=2)
tk.Label(root, text="WARNING - 0MS COULD BRICK COMPUTER DURING CLICKS", bg="black", fg="red").grid(column=1, row=4)

x_to_click.grid(row=1, column=1, padx=30)
y_to_click.grid(row=1, column=2, padx=30)
time_to_wait.grid(row=3, column=1)
clicks_amount.grid(row=3, column=2)
start_button.grid(row=1, column=3, padx=30)

root.mainloop()
