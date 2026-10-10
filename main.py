#this part of gui is made with ai not by me.
import tkinter as tk
from tkinter import messagebox

# ---------- COLORS ----------
BG = "#F5F3FF"
WHITE = "#FFFFFF"
PURPLE = "#7C3AED"
DARK_PURPLE = "#6D28D9"
TEXT = "#292344"
MUTED = "#89839F"
MINT = "#D1FAE5"
BORDER = "#E9E4F5"
RED = "#FEE2E2"

# ---------- WINDOW ----------
root = tk.Tk()
root.title("Bloom To-Do")
root.geometry("600x650")
root.minsize(450, 450)
root.configure(bg=BG)

FONT = "Segoe UI"

tasks = []

# ---------- HEADER ----------
header = tk.Frame(root, bg=BG)
header.pack(fill="x", padx=30, pady=(25, 15))

tk.Label(
    header,
    text="✦ bloom.",
    font=(FONT, 26, "bold"),
    bg=BG,
    fg=PURPLE
).pack(anchor="w")

tk.Label(
    header,
    text="A little progress every day.",
    font=(FONT, 11),
    bg=BG,
    fg=MUTED
).pack(anchor="w", pady=(3, 0))

# ---------- SUMMARY ----------
summary = tk.Frame(
    root,
    bg=WHITE,
    highlightbackground=BORDER,
    highlightthickness=1
)
summary.pack(fill="x", padx=30, pady=(0, 18))

tk.Label(
    summary,
    text="YOUR TASKS",
    font=(FONT, 9, "bold"),
    bg=WHITE,
    fg=MUTED
).pack(anchor="w", padx=15, pady=(12, 3))

count_label = tk.Label(
    summary,
    text="0 remaining · 0 total",
    font=(FONT, 15, "bold"),
    bg=WHITE,
    fg=TEXT
)
count_label.pack(anchor="w", padx=15, pady=(0, 12))

# ---------- INPUT ----------
input_frame = tk.Frame(root, bg=BG)
input_frame.pack(fill="x", padx=30, pady=(0, 20))

task_entry = tk.Entry(
    input_frame,
    font=(FONT, 11),
    bg=WHITE,
    fg=TEXT,
    insertbackground=PURPLE,
    relief="flat",
    highlightthickness=1,
    highlightbackground=BORDER,
    highlightcolor=PURPLE
)
task_entry.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=12,
    padx=(0, 10)
)

# ---------- TASK LIST ----------
tk.Label(
    root,
    text="YOUR LIST",
    font=(FONT, 10, "bold"),
    bg=BG,
    fg=TEXT
).pack(anchor="w", padx=30, pady=(0, 10))

list_container = tk.Frame(root, bg=BG)
list_container.pack(
    fill="both",
    expand=True,
    padx=30
)

canvas = tk.Canvas(
    list_container,
    bg=BG,
    highlightthickness=0
)

scrollbar = tk.Scrollbar(
    list_container,
    orient="vertical",
    command=canvas.yview
)

task_frame = tk.Frame(canvas, bg=BG)

frame_window = canvas.create_window(
    (0, 0),
    window=task_frame,
    anchor="nw"
)

canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


def update_scroll_region(event=None):
    canvas.configure(scrollregion=canvas.bbox("all"))


def resize_task_frame(event):
    canvas.itemconfigure(frame_window, width=event.width)


task_frame.bind("<Configure>", update_scroll_region)
canvas.bind("<Configure>", resize_task_frame)


# ---------- FUNCTIONS ----------
def update_tasks():
    for widget in task_frame.winfo_children():
        widget.destroy()

    remaining = sum(1 for task in tasks if not task["done"])

    count_label.config(
        text=f"{remaining} remaining · {len(tasks)} total"
    )

    if not tasks:
        tk.Label(
            task_frame,
            text="Nothing here yet 🌱\nAdd your first task above!",
            font=(FONT, 11),
            bg=BG,
            fg=MUTED,
            justify="center"
        ).pack(pady=35)
        return

    for index, task in enumerate(tasks):
        card = tk.Frame(
            task_frame,
            bg=WHITE,
            highlightbackground=BORDER,
            highlightthickness=1
        )
        card.pack(fill="x", pady=4)

        completed = tk.BooleanVar(value=task["done"])

        def toggle_task(i=index, variable=completed):
            tasks[i]["done"] = variable.get()
            update_tasks()

        checkbox = tk.Checkbutton(
            card,
            variable=completed,
            command=toggle_task,
            bg=WHITE,
            activebackground=WHITE,
            selectcolor=MINT,
            relief="flat",
            cursor="hand2"
        )
        checkbox.pack(side="left", padx=(8, 3), pady=8)

        task_label = tk.Label(
            card,
            text=task["name"],
            font=(FONT, 11),
            bg=WHITE,
            fg=MUTED if task["done"] else TEXT,
            justify="left",
            anchor="w",
            wraplength=300
        )

        if task["done"]:
            task_label.config(font=(FONT, 11, "overstrike"))

        task_label.pack(
            side="left",
            fill="x",
            expand=True,
            padx=4,
            pady=10
        )

        def delete_task(i=index):
            if messagebox.askyesno(
                "Delete task",
                "Do you want to delete this task?"
            ):
                tasks.pop(i)
                update_tasks()

        delete_button = tk.Button(
            card,
            text="✕",
            command=delete_task,
            font=(FONT, 10, "bold"),
            bg=RED,
            fg="#B91C1C",
            activebackground="#FECACA",
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=4
        )
        delete_button.pack(side="right", padx=8, pady=7)


def add_task(event=None):
    name = task_entry.get().strip()

    if not name:
        messagebox.showinfo(
            "Empty task",
            "Please enter a task first.",
            parent=root
        )
        return

    tasks.append({
        "name": name,
        "done": False
    })

    task_entry.delete(0, tk.END)
    update_tasks()
    task_entry.focus_set()


# ---------- BUTTONS ----------
add_button = tk.Button(
    input_frame,
    text="+ Add",
    command=add_task,
    font=(FONT, 10, "bold"),
    bg=PURPLE,
    fg=WHITE,
    activebackground=DARK_PURPLE,
    activeforeground=WHITE,
    relief="flat",
    cursor="hand2",
    padx=16,
    pady=10
)
add_button.pack(side="right")

task_entry.bind("<Return>", add_task)

# ---------- FOOTER ----------
tk.Label(
    root,
    text="MADE WITH ♥ AND PYTHON",
    font=(FONT, 8, "bold"),
    bg=BG,
    fg=MUTED
).pack(pady=12)

# ---------- START APP ----------
update_tasks()
task_entry.focus_set()
root.mainloop()
