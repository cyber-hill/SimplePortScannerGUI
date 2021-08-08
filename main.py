from tkinter import *
from tkinter import messagebox
import socket,os

list = []
root=Tk()
root.title('PortScanner By Cyber_Hill')
sym="~"*48
greeting = Text(background="black", width=50,height=5, foreground='red')
command=Entry(width=60, bg="white", fg="black",foreground='green',relief="solid",font=(50))
greeting.pack()
greeting.insert('1.0',f'{sym}\n[1] --- Scan One Port\n[2] --- Scan 0-1024 Ports\n[3] --- Custom Range of Port or Multiple Ports\n{sym}')
command.pack(padx=10,pady=11)
hosts = Entry(width=60, bg="white", fg="black", foreground='green', relief="solid", font=(50))
ports = Entry(width=60, bg="white", fg="black", foreground='green', relief="solid", font=(50))
hosst = Label(text="Host", width=60, foreground='black')
poort = Label(text="Port", width=60, foreground='black')
def oneport():
    scan = socket.socket()
    host = hosts.get()
    port = ports.get()
    if not host and not port:
        greeting.delete("1.0", END)
        greeting.insert("1.0","Host and Port is Empty")
    elif not host:
        greeting.delete("1.0", END)
        greeting.insert("1.0","Host is Empty")
    elif not port:
        greeting.delete("1.0", END)
        greeting.insert("1.0","Port is Empty")
    else:
        greeting.delete("1.0", END)
        try:
            port = int(port)
            greeting.delete("1.0", END)
            try:

                scan.connect((host, port))
            except socket.error:
                greeting.insert("1.0", f"[!] Port -- {port} -- [CLOSED]")
            else:
                greeting.insert("1.0", f"[!] Port -- {port} -- [OPEN]")
        except:
            greeting.insert("1.0", "Port must be number")



def listport():
    scan = socket.socket()
    host = hosts.get()
    if not host:
        greeting.delete("1.0", END)
        greeting.insert("1.0", "Host is Empty")
    else:
        greeting.delete("1.0", END)
        lists = []
        s = 80
        while s <= 90:
            lists.append(s)
            s += 1
        # port=[1,80,443]
        file = open("result.txt", "w")
        file.write(f"Scan Result\n\nHost -->  {host}\n\n")
        file.close()
        for i in lists:
            try:
                scan = socket.socket()
                scan.settimeout(0.5)
                scan.connect((host, i))
            except socket.error:
                pass
            else:
                greeting.insert("1.0", f"[!] Port -- {i} -- [OPEN]\n")
                file = open("result.txt", "a")
                file.write("Port -- " + str(i) + " -- [OPEN]\n")
                file.close()
        cvd = os.getcwd()
        messagebox.showinfo("Success", f"Սկանավորման արդյունքը հաջողությամբ պահպանվել է\nՖայլի գտնվելու վայրը։ {cvd}"+r'\result.txt')
def customport():
    host = hosts.get()
    port = ports.get()
    if not host and not port:
        greeting.delete("1.0", END)
        greeting.insert("1.0", "Host and Port is Empty")
    elif not host:
        greeting.delete("1.0", END)
        greeting.insert("1.0", "Host is Empty")
    elif not port:
        greeting.delete("1.0", END)
        greeting.insert("1.0", "Port is Empty")
    else:
        greeting.delete("1.0", END)
        list = []
        try:
            if '-' in port:
                b = port.split('-')
                b[0] = int(b[0])
                b[1] = int(b[1])
                b[1] = b[1] + 1
                l = range(b[0], b[1])
                for num in l:
                    list.append(num)

                file = open("result.txt", "w")
                file.write(f"Scan Result\n\nHost -->  {host}\n\n")
                file.close()
                for i in list:
                    try:
                        scan = socket.socket()
                        scan.settimeout(0.5)
                        scan.connect((host, i))
                    except socket.error:
                        pass
                    else:
                        greeting.insert("1.0", f"[!] Port -- {i} -- [OPEN]\n")
                        file = open("result.txt", "a")
                        file.write("Port -- " + str(i) + " -- [OPEN]\n")
                        file.close()
                cvd = os.getcwd()
                messagebox.showinfo("Success",f"Սկանավորման արդյունքը հաջողությամբ պահպանվել է\nՖայլի գտնվելու վայրը։ {cvd}" + r'\result.txt')
            elif ',' in port:
                b = port.split(',')
                for num in b:
                    num = int(num)
                    list.append(num)

                file = open("result.txt", "w")
                file.write(f"Scan Result\n\nHost -->  {host}\n\n")
                file.close()
                for i in list:
                    try:
                        scan = socket.socket()
                        scan.settimeout(0.5)
                        scan.connect((host, i))
                    except socket.error:
                        pass
                    else:
                        greeting.insert("1.0", f"[!] Port -- {i} -- [OPEN]\n")
                        file = open("result.txt", "a")
                        file.write("Port -- " + str(i) + " -- [OPEN]\n")
                        file.close()
                cvd = os.getcwd()
                messagebox.showinfo("Success",f"Սկանավորման արդյունքը հաջողությամբ պահպանվել է\nՖայլի գտնվելու վայրը։ {cvd}" + r'\result.txt')
            else:
                greeting.delete("1.0", END)
                greeting.insert("1.0","Error!")
        except:
            greeting.delete("1.0", END)
            greeting.insert("1.0", "Error!")
def neext():
    com=command.get()
    command.delete(0,END)
    def func1():
        greeting.delete("1.0",END)
        button.destroy()
        greeting.insert("1.0","Please Write Host and Port ")
        command.destroy()
        hosst.pack()
        hosts.pack()
        poort.pack()
        ports.pack()
        buttononeport.pack(pady=5)

    def func2():
        greeting.delete("1.0",END)
        button.destroy()
        greeting.insert("1.0","Please Write Host")
        command.destroy()
        hosst.pack()
        hosts.pack()
        buttonlistport.pack(pady=5)
    def func3():
        greeting.delete("1.0",END)
        button.destroy()
        greeting.insert("1.0","Please Write Host and Port ")
        command.destroy()
        hosst.pack()
        hosts.pack()
        poort.pack()
        ports.pack()
        buttoncustomport.pack(pady=5)
    if com == "1":
        func1()
    elif com == "2":
        func2()
    elif com == "3":
        func3()
    elif not com:
        greeting.delete("1.0", END)
        greeting.insert('1.0',f'!Error:Entry is empty\n[1] --- Scan One Port\n[2] --- Scan 0-1024 Ports\n[3] --- Custom Range of Port or Multiple Ports\n{sym}')

    else:
        greeting.delete("1.0", END)
        greeting.insert('1.0',f'!Error:Please enter a valid menu number\n[1] --- Scan One Port\n[2] --- Scan 0-1024 Ports\n[3] --- Custom Range of Port or Multiple Ports\n{sym}')


button=Button(text="✔",font=(180),relief='ridge',activeforeground='green',command=neext)
buttononeport=Button(text="✔",font=(180),relief='ridge',activeforeground='green',command=oneport)
buttonlistport=Button(text="✔",font=(180),relief='ridge',activeforeground='green',command=listport)
buttoncustomport=Button(text="✔",font=(180),relief='ridge',activeforeground='green',command=customport)
# buttonsearch=Button(text="✔",font=(180),command=search)
# buttononeport.pack(padx=100,side="right")
button.pack()
def aboutus():
    messagebox.showinfo("About", "PortScanner By Cyber_Hill\nTelegram:@Cyber_Hill")
def appexit():
    root.destroy()
main_menu = Menu()
file_menu = Menu(tearoff=0)
file_menu.add_command(label="About",command=aboutus)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=appexit)
main_menu.add_cascade(label="File",menu=file_menu)
root.config(menu=main_menu)
root.geometry("400x350")
root.resizable(False,False)
root.mainloop()