import tkinter as tk

def show_order():
    selection = str(var.get())
    label.config(text="You ordered " + selection + ".")


root = tk.Tk()
root.title("Restaurant Menu")


var = tk.IntVar()


pasta_btn = tk.Radiobutton(root, text="Pasta - 10₹", variable=var, value=1, command=show_order)
pizza_btn = tk.Radiobutton(root, text="Pizza - 12₹", variable=var, value=2, command=show_order)
salad_btn = tk.Radiobutton(root, text="Salad - 8₹", variable=var, value=3, command=show_order)


pasta_btn.pack()
pizza_btn.pack()
salad_btn.pack()


label = tk.Label(root)
label.pack()


root.mainloop()