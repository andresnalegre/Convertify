import tkinter as tk
from tkinter import filedialog, messagebox
import aspose.words as aw #type: ignore


def select_file():
    input_file = filedialog.askopenfilename(
        title="Select PNG File",
        filetypes=[("PNG Files", "*.png")]
    )
    if input_file:
        entry_input.delete(0, tk.END)
        entry_input.insert(0, input_file)


def select_destination():
    output_file = filedialog.asksaveasfilename(
        title="Save SVG As",
        defaultextension=".svg",
        filetypes=[("SVG Files", "*.svg")]
    )
    if output_file:
        entry_output.delete(0, tk.END)
        entry_output.insert(0, output_file)


def convert():
    png = entry_input.get()
    svg = entry_output.get()
    
    if not png or not svg:
        messagebox.showwarning("Warning", "Please select input and output files")
        return
    
    try:
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        
        shape = builder.insert_image(png)
        save_options = aw.saving.ImageSaveOptions(aw.SaveFormat.SVG)
        shape.get_shape_renderer().save(svg, save_options)
        
        status_label.config(text="Conversion completed!")
        messagebox.showinfo("Success", "Conversion completed!")
    except Exception as e:
        status_label.config(text="Error")
        messagebox.showerror("Error", f"Error during conversion: {str(e)}")


window = tk.Tk()
window.title("Convertify")
window.geometry("500x300")
window.configure(bg="#2d2d2d")
window.resizable(False, False)

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = int((screen_width - 500) / 2)
y_coordinate = int((screen_height - 300) / 2)
window.geometry(f"500x300+{x_coordinate}+{y_coordinate}")

main_frame = tk.Frame(window, bg="#2d2d2d", padx=30, pady=30)
main_frame.pack(expand=True, fill=tk.BOTH)

title_label = tk.Label(
    main_frame, 
    text="PNG to SVG",
    font=("Helvetica", 16, "bold"),
    bg="#2d2d2d",
    fg="#ffffff"
)
title_label.pack(pady=(0, 30))

input_frame = tk.Frame(main_frame, bg="#2d2d2d")
input_frame.pack(fill=tk.X, pady=5)

input_label = tk.Label(
    input_frame, 
    text="PNG File:",
    font=("Helvetica", 10),
    bg="#2d2d2d",
    fg="#ffffff",
    width=10,
    anchor="w"
)
input_label.pack(side=tk.LEFT, padx=(0, 5))

entry_input = tk.Entry(
    input_frame,
    font=("Helvetica", 10),
    bg="#3d3d3d",
    fg="#ffffff",
    insertbackground="#ffffff",
    relief=tk.FLAT,
    highlightthickness=1,
    highlightbackground="#3d3d3d",
    highlightcolor="#5d5d5d"
)
entry_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

browse_input_btn = tk.Button(
    input_frame,
    text="Browse",
    font=("Helvetica", 9),
    bg="#ffffff",
    fg="#000000",
    relief=tk.FLAT,
    padx=10,
    command=select_file
)
browse_input_btn.pack(side=tk.LEFT)

output_frame = tk.Frame(main_frame, bg="#2d2d2d")
output_frame.pack(fill=tk.X, pady=15)

output_label = tk.Label(
    output_frame, 
    text="Save SVG:",
    font=("Helvetica", 10),
    bg="#2d2d2d",
    fg="#ffffff",
    width=10,
    anchor="w"
)
output_label.pack(side=tk.LEFT, padx=(0, 5))

entry_output = tk.Entry(
    output_frame,
    font=("Helvetica", 10),
    bg="#3d3d3d",
    fg="#ffffff",
    insertbackground="#ffffff",
    relief=tk.FLAT,
    highlightthickness=1,
    highlightbackground="#3d3d3d",
    highlightcolor="#5d5d5d"
)
entry_output.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

browse_output_btn = tk.Button(
    output_frame,
    text="Browse",
    font=("Helvetica", 9),
    bg="#ffffff",
    fg="#000000",
    relief=tk.FLAT,
    padx=10,
    command=select_destination
)
browse_output_btn.pack(side=tk.LEFT)

convert_btn = tk.Button(
    main_frame,
    text="CONVERT",
    font=("Helvetica", 10, "bold"),
    bg="#e0e0e0",
    fg="#000000",
    activebackground="#ffffff",
    activeforeground="#000000",
    relief=tk.FLAT,
    padx=30,
    pady=8,
    command=convert
)
convert_btn.pack(pady=25)

status_label = tk.Label(
    window,
    text="Ready",
    bg="#222222",
    fg="#aaaaaa",
    font=("Helvetica", 8),
    anchor="w",
    padx=10,
    pady=3
)
status_label.pack(side=tk.BOTTOM, fill=tk.X)

window.mainloop()