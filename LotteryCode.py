from tkinter import *;
from tkinter import messagebox;
from random import *;

data = {};

root = Tk();

indx = 0;


def exitButtonAction(root):
    if messagebox.askokcancel("Exit", "Do you want to Exit?"):
        root.quit();
        root.destroy();

def winner(master):
    global data;
    global indx;
    master.quit();
    #master.withdraw();

    master = Tk();
    master.geometry("350x250");
    master.title("Winner");

    randval = randint(1, indx);

    print(indx , randval);

    detail = "Congratulations !!!\n" + data[randval][0] + "\nYour Mobile Number is\n" + data[randval][1];

    winnerLabel = Label(master, text = detail, font="arial 12 bold", fg="red");
    winnerLabel.place(relx=0.5, rely=0.5, anchor = "center");

    exitButton = Button(master, text="Exit", bg="red", fg="black", width=5, command=lambda : exitButtonAction(master));
    exitButton.place(relx=0.8, rely=0.0);

    master.resizable(False, False);
    master.mainloop();


def got_to_draw():
    global indx
    global data;

    master = Tk();
    master.geometry("350x250")
    master.title("Lottery Draw");

    clickButton = Button(master, text = "Just Click it", width = 30, font = "arial 10 bold", bg = "black", fg = "white", command=lambda : winner(master));
    clickButton.place(relx=0.5, rely=0.5, anchor = "center");

    exitButton = Button(master, text="Exit", bg="red", fg="black", width=5, command=lambda : exitButtonAction(master));
    exitButton.place(relx=0.8, rely=0.0);

    master.resizable(False, False);
    master.mainloop();

def drawButtonAction():
    global data;
    global indx;
    if(len(data) >= 2):
        got_to_draw();
    else:
        messagebox.showerror("Error", "Draw will not be happened due to insufficient member")

def show_the_list():
    master = Tk();
    master.title("Member List");
    master.geometry("350x250");

    scroll = Scrollbar(master);
    scroll.pack(side=RIGHT, fill=Y);

    listbox = Listbox(master, height=15, width=40, yscrollcommand=scroll.set);
    listbox.place(relx=0.5, rely=0.5, anchor="center")

    scroll.config(command=listbox.yview)

    cnt = 1;

    for i in range(1 , indx+1):
        name = data[i][0];
        mobile = data[i][1];
        listbox.insert(END, str(cnt) + ". " + name + "  ---  " + mobile);
        cnt += 1;

    master.resizable(False, False);
    master.mainloop();

def submitAction(uname, password, master):
    if(uname == "admin" and password=="admin"):
        master.quit();
        master.withdraw();
        show_the_list();
    else:
        messagebox.showerror("Error", "Wrong username or password")


def change_window(master):
    master.quit();
    master.withdraw();
    aWindow = Toplevel(root);
    aWindow.destroy();
    root.iconify();
    root.deiconify();

def insertInfo(name, mobile, name_event, mobile_event, master):
    global indx;
    global data;
    def stayInsertInfo(name=name, mobile=mobile, name_event=name_event, mobile_event = mobile_event, master = master):
        global indx;
        global data;
        name_event.delete(0, END);
        mobile_event.delete(0, END);
        name = str(name);
        mobile = str(mobile);
        indx += 1;
        data.setdefault(indx, []).append(name);
        data.setdefault(indx, []).append(mobile);
        messagebox.showinfo("insertInfo", str(indx) + ". Insertion Successful!!")
        #messagebox._show("Insertion", str(indx) + ". Insertion Successful!!")

    stayInsertInfo(name, mobile, name_event, mobile_event, master);

def listShow():
    master = Tk();
    master.title("Admin Panel");
    master.geometry("350x250");

    unameLabel = Label(master, text="Username", font = "arial 10");
    unameLabel.place(relx=0.5, rely=0.2, anchor="center");

    unameEntry = Entry(master);
    unameEntry.place(relx=0.5, rely=0.3, anchor="center");

    passLabel = Label(master, text="Password", font="arial 10");
    passLabel.place(relx=0.5, rely=0.5, anchor="center");

    passEntry = Entry(master, show="*");
    passEntry.place(relx=0.5, rely=0.6, anchor="center");

    submitButton = Button(master, text="Submit", command = lambda : submitAction(unameEntry.get(), passEntry.get(), master));
    submitButton.place(relx=0.5, rely=0.8, anchor="center");


def insertButtonAction():
    root.withdraw();
    master = Tk();
    master.title("Data Entry");
    master.geometry("350x250+200+250");

    # Start the main code for insertButtonAction

    nameLabel = Label(master, text="Enter Your Name: ");
    nameLabel.place(relx=0.5, rely=0.2, anchor="center");

    nameEntry = Entry(master);
    nameEntry.place(relx=0.5, rely=0.3, anchor="center");

    mobileNumberLabel = Label(master, text = "Enter your Mobile Number: ");
    mobileNumberLabel.place(relx=0.5, rely=0.5, anchor="center");

    mobileNumberEntry = Entry(master);
    mobileNumberEntry.place(relx=0.5, rely=0.6, anchor="center");

    nameEntry.delete(0, END);
    mobileNumberEntry.delete(0, END);

    insertButton = Button(master, text="Insert", command = lambda : insertInfo(nameEntry.get(), mobileNumberEntry.get(), nameEntry, mobileNumberEntry, master));
    insertButton.config(font="times 10 bold", bg="white", fg="black")
    insertButton.place(relx=0.3, rely=0.8, anchor="center");

    showListButton = Button(master, text="Show List", command = listShow);
    showListButton.config(font="times 10 bold", bg="white", fg="black")
    showListButton.place(relx=0.6, rely=0.8, anchor="center")

    backButton = Button(master, text = "<<Back", fg="black", font="bold 10", width = 5, command = lambda : change_window(master));
    backButton.place(relx=0.0, rely=0.0);

    master.resizable(False, False);
    master.mainloop();

root.title("Lottery Software");
root.geometry("350x250+200+250");

insertButton = Button(root, text = "Insert", width = 20, font="arial 10 bold", bg="black", fg="white", command = insertButtonAction);
insertButton.place(relx = 0.5, rely = 0.4, anchor = "center")

drawButton = Button(root, text = "Draw", bg = "light gray", font = "arial 10 bold", width = 20, command = drawButtonAction);
drawButton.place(relx = 0.5, rely = 0.6, anchor = "center")

exitButton = Button(root, text="Exit", bg="red", fg="black", width = 5, command = lambda : exitButtonAction(root));
exitButton.place(relx = 0.8, rely=0.0);


root.resizable(False, False);
root.mainloop();

# use lambda when you are sending parameters otherwise no need to use.