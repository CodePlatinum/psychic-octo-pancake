import customtkinter as ctk


app = ctk.CTk()
app.title("Calculator")
app.geometry("320x450")


def set_theme(theme):
    colors = {
        "Light": ("white", "black"),
        "Dark": ("black", "#333333"),
        "System": ("gray", "#A0A0A0"),
        "Blue": ("blue", "#5A9BD5"),
        "Green": ("green", "#4CAF50"),
        "Purple": ("purple", "#9370DB")
    }
    bg_color, btn_color = colors.get(theme, ("white", "#E0E0E0"))
    app.configure(fg_color=bg_color)
    for btn in button_widgets:
        btn.configure(fg_color=btn_color)


entry = ctk.CTkEntry(app, width=280, font=("Arial", 24), justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)


def on_button_click(value):
    if value == "=":
        try:
            entry.insert("end", " = " + str(eval(entry.get())))
        except Exception:
            entry.insert("end", " Error")
    elif value == "C":
        entry.delete(0, "end")
    else:
        entry.insert("end", value)


buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
    ["(", ")"]
]

button_widgets = []
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        btn = ctk.CTkButton(app, text=text, width=70, height=60, font=("Arial", 18), command=lambda v=text: on_button_click(v))
        btn.grid(row=i + 1, column=j, padx=5, pady=5)
        button_widgets.append(btn)


menu = ctk.CTkOptionMenu(app, values=["Light", "Dark", "Blue", "Green", "Purple"], command=set_theme, width=180)
menu.grid(row=6, column=0, columnspan=4, pady=10, padx=10)
menu.set("Theme")


app.mainloop()
