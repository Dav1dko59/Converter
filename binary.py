import math
import tkinter as tk

window = tk.Tk()
window.title("Converter")
window.geometry("720x480")
window.configure(bg="#1e1e1e")  # Tmavé pozadí okna

def zobraz(frame):
    frame.tkraise()

container =tk.Frame(window)
container.pack(fill="both", expand=True)

app1 = tk.Frame(container,bg="lightblue")
app2 = tk.Frame(container,bg="lightgreen")

for frame in (app1,app2):
    frame.place(relwidth=1,relheight=1)

label1 = tk.Label(app1,text="Decimal to Binary", font=("Arial", 20))
label1.pack(pady=10)
button1 = tk.Button(app1, text="Binary to Decimal",command=lambda: zobraz(app2))
button1.pack()

label2 = tk.Label(app2,text="Binary to Decimal",font=("Arial", 20))
label2.pack(pady=10)
button2 = tk.Button(app2, text="Decimal to Binary",command=lambda: zobraz(app1))
button2.pack()

def binary():
    vstup_text = vstup.get()
    try:
        if not vstup_text.strip():
            raise ValueError("Vstup nebyl zadán.")
        number = int(vstup.get())
        if number < 0:
            raise ValueError("Zadej kladné číslo.")
        
    except ValueError as e:
        output_bin.config(text=f"Chyba: {e}", fg="red", bg="lightblue")

    else:
        lst = []
        while(number > 0):
            x = int(number % 2)
            lst.append(x)
            number = int(number / 2)

        lst.reverse()
        output_bin.config(text="".join(map(str,lst)), fg="#083B2A", bg="lightblue")

def decimal():
    vstup_text1 = vstup1.get()
    try:
        if not vstup_text1.strip():
            raise ValueError("Vstup nebyl zadán.")
        number1 = int(vstup1.get())
        if number1 < 0:
            raise ValueError("Zadej kladné číslo.")
        o = list(map(int,list(vstup_text1.strip())))
        for each in o:
            if each != 1 and each != 0:
                raise ValueError("Zadávej pouze 1 nebo 0.")
        
    except ValueError as e:
        output_dec.config(text=f"Chyba: {e}", fg="red", bg="lightblue")

    else:
        lst1 = list(map(int,list(vstup_text1.strip())))
        result = 0
        rev_lst = lst1[::-1]
        for i in range(len(rev_lst)):
            if(rev_lst[i]==0):
                continue
            else:
                result = result + int(math.pow(2,i))
        output_dec.config(text=result,fg="#000000", bg="lightgreen")



# Vstup
vstup = tk.Entry(app1, width=20, font=("Arial", 16), bg="#eeeeee", fg="#333333")
vstup.pack(pady=20)

# Tlačítko
bttn = tk.Button(app1, text="Convert!", command=binary,
                 font=("Arial", 14), bg="#4CAF50", fg="white", width=15, height=2)
bttn.pack(pady=10)

# Výstup
output_bin = tk.Label(app1, text="", font=("Consolas", 18), bg="lightblue", fg="white")
output_bin.pack(pady=30)

vstup1 = tk.Entry(app2, width=20, font=("Arial", 16), bg="#eeeeee", fg="#333333")
vstup1.pack(pady=20)

bttn1 = tk.Button(app2, text="Convert!", command=decimal,
                 font=("Arial", 14), bg="#4CAF50", fg="white", width=15, height=2)
bttn1.pack(pady=10)

output_dec = tk.Label(app2,text="", font=("Consolas", 18), bg="lightgreen", fg="white")
output_dec.pack(pady=50)

zobraz(app1)
window.mainloop()
