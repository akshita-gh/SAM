import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import storage

# ---------------------- Colors ----------------------

BG = "#EEF4FB"
CARD = "#FFFFFF"
TEXT = "#081B45"
SUBTEXT = "#56657F"
BLUE = "#2D6DF6"

# ---------------------- Functions ----------------------


def new_registration():
    messagebox.showinfo(
        "Registration",
        "New Registration Module"
    )


def login():
    messagebox.showinfo(
        "Login",
        "Login Module"
    )


def teacher_dashboard(root):

    win = tk.Toplevel(root)

    win.title("Teacher Dashboard")

    win.geometry("900x550")

    win.configure(bg="white")

    title = tk.Label(
        win,
        text="Attendance Records",
        bg="white",
        fg=TEXT,
        font=("Segoe UI", 22, "bold")
    )

    title.pack(pady=20)

    style = ttk.Style()

    style.theme_use("default")

    style.configure(
        "Treeview",
        font=("Segoe UI", 11),
        rowheight=34
    )

    style.configure(
        "Treeview.Heading",
        font=("Segoe UI", 12, "bold")
    )

    tree = ttk.Treeview(
        win,
        columns=("Name", "Date", "Time"),
        show="headings"
    )

    tree.heading("Name", text="Name")
    tree.heading("Date", text="Date")
    tree.heading("Time", text="Time")

    tree.column("Name", width=250)

    tree.column("Date", width=180)

    tree.column("Time", width=180)

    records = storage.get_attendance_records()

    for row in records:

        tree.insert("", tk.END, values=row)

    tree.pack(fill="both", expand=True, padx=30, pady=20)


# ---------------------- Card ----------------------


def create_card(parent, icon, title, subtitle, command):

    outer = tk.Frame(
        parent,
        bg="#FDFDFD",
        highlightbackground="#E7EBF2",
        highlightthickness=1
    )

    outer.pack(fill="x", pady=16)

    left_icon = tk.Frame(
        outer,
        width=95,
        height=95,
        bg="#EAF2FF"
    )

    left_icon.pack(
        side="left",
        padx=22,
        pady=18
    )

    left_icon.pack_propagate(False)

    tk.Label(
        left_icon,
        text=icon,
        bg="#EAF2FF",
        fg=BLUE,
        font=("Segoe UI Emoji", 32)
    ).pack(expand=True)

    middle = tk.Frame(
        outer,
        bg="#FDFDFD"
    )

    middle.pack(
        side="left",
        padx=5,
        pady=20
    )

    tk.Label(
        middle,
        text=title,
        bg="#FDFDFD",
        fg=TEXT,
        font=("Segoe UI", 20, "bold")
    ).pack(anchor="w")

    tk.Label(
        middle,
        text=subtitle,
        justify="left",
        bg="#FDFDFD",
        fg=SUBTEXT,
        font=("Segoe UI", 12)
    ).pack(anchor="w", pady=5)

    tk.Button(
        outer,
        text="❯",
        bg="#FDFDFD",
        fg="#56657F",
        bd=0,
        cursor="hand2",
        font=("Segoe UI", 24),
        command=command
    ).pack(side="right", padx=30)


# ---------------------- Main Window ----------------------


def main_window():

    root = tk.Tk()

    root.title("SAM")

    root.geometry("1600x980")

    root.configure(bg=BG)

    root.resizable(False, False)

    # ---------------- Left ----------------

    left = tk.Frame(
        root,
        bg=BG,
        width=650
    )

    left.pack(
        side="left",
        fill="both",
        padx=50,
        pady=35
    )

    logo_box = tk.Frame(
        left,
        width=95,
        height=95,
        bg="white"
    )

    logo_box.pack(anchor="w")

    logo_box.pack_propagate(False)

    tk.Label(
        logo_box,
        text="👤",
        bg="white",
        fg=BLUE,
        font=("Segoe UI Emoji", 38)
    ).pack(expand=True)

    tk.Label(
        left,
        text="SAM",
        bg=BG,
        fg=TEXT,
        font=("Segoe UI", 60, "bold")
    ).pack(anchor="w", pady=(18, 0))

    tk.Label(
        left,
        text="Smart Attendance\nManagement System",
        justify="left",
        bg=BG,
        fg=BLUE,
        font=("Segoe UI", 34, "bold")
    ).pack(anchor="w")

    tk.Label(
        left,
        text="A smart and secure way to take attendance\nusing facial recognition technology.",
        justify="left",
        bg=BG,
        fg=SUBTEXT,
        font=("Segoe UI", 16)
    ).pack(anchor="w", pady=20)

    try:

        image = Image.open("assets/girl.png")

        image = image.resize((470, 560))

        photo = ImageTk.PhotoImage(image)

        img = tk.Label(
            left,
            image=photo,
            bg=BG
        )

        img.image = photo

        img.pack(anchor="w", pady=15)

    except:

        holder = tk.Frame(
            left,
            width=470,
            height=560,
            bg="#DDE8F9"
        )

        holder.pack(anchor="w", pady=20)

        holder.pack_propagate(False)

        tk.Label(
            holder,
            text="Place girl.png\ninside assets folder",
            bg="#DDE8F9",
            fg="#64748B",
            font=("Segoe UI", 18)
        ).pack(expand=True)

    # -------- Right Panel starts here --------

    right = tk.Frame(
        root,
        bg="white",
        width=760
    )

    right.pack(
        side="right",
        fill="y",
        padx=40,
        pady=40
    )

        # ---------------- Welcome Section ----------------

    tk.Label(
        right,
        text="Welcome!",
        bg="white",
        fg=TEXT,
        font=("Segoe UI", 38, "bold")
    ).pack(pady=(45, 5))

    tk.Label(
        right,
        text="Choose an option to continue",
        bg="white",
        fg=SUBTEXT,
        font=("Segoe UI", 18)
    ).pack(pady=(0, 35))

    # ---------------- Registration Card ----------------

    create_card(
        right,
        "👤",
        "New Registration",
        "Register a new user\nfor the attendance system",
        new_registration
    )

    # ---------------- Login Card ----------------

    create_card(
        right,
        "🔒",
        "Login",
        "Login with your credentials\nto mark attendance",
        login
    )

    # ---------------- Teacher Dashboard Card ----------------

    create_card(
        right,
        "📊",
        "Teacher Dashboard",
        "Access teacher dashboard\nto manage attendance",
        lambda: teacher_dashboard(root)
    )

    # ---------------- Footer ----------------

    footer = tk.Frame(
        right,
        bg="white"
    )

    footer.pack(
        side="bottom",
        pady=35
    )

    shield = tk.Label(
        footer,
        text="🛡",
        bg="white",
        fg=BLUE,
        font=("Segoe UI Emoji", 20)
    )

    shield.pack(side="left", padx=5)

    tk.Label(
        footer,
        text="Secure  •  Accurate  •  Efficient",
        bg="white",
        fg=SUBTEXT,
        font=("Segoe UI", 16)
    ).pack(side="left")

    # ---------------- Hover Effects ----------------

    def enable_hover(widget):

        def enter(e):
            widget.configure(bg="#F7FAFF")

        def leave(e):
            widget.configure(bg="#FDFDFD")

        widget.bind("<Enter>", enter)
        widget.bind("<Leave>", leave)

    for child in right.winfo_children():

        if isinstance(child, tk.Frame):

            enable_hover(child)

    root.mainloop()


# ---------------- Run ----------------

if __name__ == "__main__":

    main_window()