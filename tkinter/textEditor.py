import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Menu status states
FILE_OPEN = False
EDIT_OPEN = False
FORMAT_OPEN = False
VIEW_OPEN = False
HELP_OPEN = False

window = tk.Tk()
frm_file = tk.Frame(window)
frm_edit = tk.Frame(window)
frm_format = tk.Frame(window)
frm_view = tk.Frame(window)
frm_help = tk.Frame(window)

# METHODS
def on_click_file():
    global FILE_OPEN, frm_file

    if FILE_OPEN:
        frm_file.destroy()
        FILE_OPEN = False
    else:
        FILE_OPEN = True
        frm_file = tk.Frame(window, relief=tk.SUNKEN)
        btn_new = tk.Button(frm_file, text="New", command=new)
        btn_open = tk.Button(frm_file, text="Open", command=open_file)
        btn_save = tk.Button(frm_file, text="Save")
        btn_save_as = tk.Button(frm_file, text="Save as...", command=save_file_as)
        btn_new.pack(fill=tk.X)
        btn_open.pack(fill=tk.X)
        btn_save.pack(fill=tk.X)
        btn_save_as.pack(fill=tk.X)
        frm_file.place(x=btn_file.winfo_rootx() - 50, y=25)
    return

def new():
    close_all_menus()
    txt_edit.delete(0.0, tk.END)
    window.title("Text Editor")

def undo(*args):
    close_all_menus()
def cut(*args):
    close_all_menus()
def copy(*args):
    close_all_menus()
def paste(*args):
    close_all_menus()

def on_click_edit():
    global EDIT_OPEN, frm_edit

    if EDIT_OPEN:
        frm_edit.destroy()
        EDIT_OPEN = False
    else:
        EDIT_OPEN = True
        frm_edit = tk.Frame(window, relief=tk.SUNKEN)
        btn_undo = tk.Button(frm_edit, text="Undo", command=undo)
        btn_cut = tk.Button(frm_edit, text="Cut", command=cut)
        btn_copy = tk.Button(frm_edit, text="Copy", command=copy)
        btn_paste = tk.Button(frm_edit, text="Paste", command=paste)
        btn_undo.pack(fill=tk.X)
        btn_cut.pack(fill=tk.X)
        btn_copy.pack(fill=tk.X)
        btn_paste.pack(fill=tk.X)
        frm_edit.place(x=btn_edit.winfo_rootx()-50, y=25)
    return

def on_click_format():
    global FORMAT_OPEN, frm_format

    if FORMAT_OPEN:
        frm_format.destroy()
        FORMAT_OPEN = False
    else:
        FORMAT_OPEN = True
        frm_format = tk.Frame(window, relief=tk.SUNKEN)
        btn_beta = tk.Button(frm_format, text="Beta Feature - Not yet implemented")
        btn_beta.pack(fill=tk.X)
        frm_format.place(x=btn_format.winfo_rootx()-50, y=25)
    return
def on_click_view():
    global VIEW_OPEN, frm_view

    if VIEW_OPEN:
        frm_view.destroy()
        VIEW_OPEN = False
    else:
        VIEW_OPEN = True
        frm_view = tk.Frame(window, relief=tk.SUNKEN)
        btn_beta = tk.Button(frm_view, text="Beta Feature - Not yet implemented")
        btn_beta.pack(fill=tk.X)
        frm_view.place(x=btn_view.winfo_rootx()-50, y=25)
    return
def on_click_help():
    global HELP_OPEN, frm_help

    if HELP_OPEN:
        frm_help.destroy()
        HELP_OPEN = False
    else:
        HELP_OPEN = True
        frm_help = tk.Frame(window, relief=tk.SUNKEN)
        btn_beta = tk.Button(frm_help, text="Beta Feature - Not yet implemented")
        btn_beta.pack(fill=tk.X)
        frm_help.place(x=btn_help.winfo_rootx()-50, y=25)
    return

def open_file(*args):
    """Open a file for editing."""
    global FILE_OPEN, frm_file
    if FILE_OPEN:
        FILE_OPEN = False
        frm_file.destroy()

    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Text Editor - {filepath}")

def save_file_as(*args):
    """Save the current file as a new file."""
    global FILE_OPEN, frm_file
    if FILE_OPEN:
        FILE_OPEN = False
        frm_file.destroy()
    
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Text Editor - {filepath}")

def quit_out(*args):
    window.quit()

def close_all_menus(*args):
    global FILE_OPEN, EDIT_OPEN, FORMAT_OPEN, VIEW_OPEN, HELP_OPEN
    global frm_file, frm_edit, frm_format, frm_view, frm_help

    if FILE_OPEN:
        FILE_OPEN = False
        frm_file.destroy()

    if EDIT_OPEN:
        EDIT_OPEN = False
        frm_edit.destroy()

    if FORMAT_OPEN:
        FORMAT_OPEN = False
        frm_format.destroy()

    if VIEW_OPEN:
        VIEW_OPEN = False
        frm_view.destroy()

    if HELP_OPEN:
        HELP_OPEN = False
        frm_help.destroy()


# GUI
window.title("Text Editor")

window.rowconfigure(1, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

frm_lower = tk.Frame(window)

txt_edit = tk.Text(frm_lower)

#Side buttons
frm_buttons = tk.Frame(frm_lower, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Open", command=open_file)
btn_save = tk.Button(frm_buttons, text="Save As...", command=save_file_as)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

#Header buttons
frm_headerbar = tk.Frame(window, relief=tk.RAISED, bd = 2, )
btn_file = tk.Button(frm_headerbar, text="File", command=on_click_file)
btn_edit = tk.Button(frm_headerbar, text="Edit", command=on_click_edit)
btn_format = tk.Button(frm_headerbar, text="Format", command=on_click_format)
btn_view = tk.Button(frm_headerbar, text="View", command=on_click_view)
btn_help = tk.Button(frm_headerbar, text="Help", command=on_click_help)

btn_file.pack(side="left")
btn_edit.pack(side="left")
btn_format.pack(side="left")
btn_view.pack(side="left")
btn_help.pack(side="left")

frm_headerbar.pack()
frm_buttons.grid(row=1, column=0, sticky="ns")
txt_edit.grid(row=1, column=1, sticky="nsew")
frm_lower.pack()

window.bind("<Control-o>", open_file)
window.bind("<Control-s>", save_file_as)
window.bind("<Control-q>", quit_out)
#window.bind("<ButtonPress-1>", close_all_menus)

window.mainloop()