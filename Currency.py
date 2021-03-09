from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import requests

try:
    api_key="Enter your key here"
    response = requests.get(f"http://data.fixer.io/api/latest?access_key={api_key}&format=1")
except requests.exceptions.ConnectionError:
    msg.showerror("Connection error", "Please check your internet Connection")
else:
    content = response.json()
    if not content["success"]:
        msg.showerror("Failiure", "Please Check your API key!")

    root = Tk()
    root.geometry("700x400")
    root.config(bg="navy")


    def convert():
        global content, converted
        try:
            inpt = float(inp.get())
        except TclError:
            pass
        else:
            base = base_combo.get()
            semi = 1 / content["rates"][base]
            converted.set(semi * inpt * content["rates"][converting_combo.get()])


    converted = DoubleVar()
    inp = DoubleVar()

    Label(root, text="Your Amount :", font=('Bahnschrift semibold SemiCondensed', 20),
          bg="navy", fg="#ffee58").place(x=50, y=100)
    Label(root, text="Converted Amount :", font=('Bahnschrift semibold SemiCondensed', 20), bg="navy",
          fg="#ffee58").place(x=50, y=200)

    Entry(root, textvariable=inp, font=('Bahnschrift semibold SemiCondensed', 18), width=10, bd=4).place(x=300, y=100)
    Entry(root, state="readonly", textvariable=converted, font=('Bahnschrift semibold SemiCondensed', 18), width=10,
          bd=4).place(x=300, y=200)

    base_combo = ttk.Combobox(root, values=tuple(content["rates"].keys()), width=4, state="readonly",
                              font=('Bahnschrift semibold SemiCondensed', 17))
    base_combo.place(y=100, x=500)
    converting_combo = ttk.Combobox(root, values=tuple(content["rates"].keys()), width=4, state="readonly",
                                    font=('Bahnschrift semibold SemiCondensed', 17))
    converting_combo.place(y=200, x=500)

    base_combo.set("INR")
    converting_combo.set("USD")

    Button(root, text="Convert", font=('Bahnschrift semibold SemiCondensed', 17), bg='#ffee58', fg="navy",
           command=convert).place(x=300, y=300)
    root.mainloop()
