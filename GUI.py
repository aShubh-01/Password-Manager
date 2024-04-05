import tkinter as tk
from manager import add, view, masterPwd
from tkinter import scrolledtext as st

def viewScreen() :
    for widget in root.winfo_children() :
        widget.destroy()
    
    displayData = st.ScrolledText(root, bg='#363636', wrap=tk.WORD, height=12, width=72)
    displayData.pack(padx=5,pady=10)
    displayData.tag_configure('styleText', font=('Consolas', 14), foreground="white")

    backButton2 = tk.Button(root, text="Back", width="8", height="2", font=("Consolas", 18, "bold"), fg="white", bg="#2D2826", command=managerScreen)
    backButton2.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    lines = view()
    
    for line in lines :
        displayData.insert(tk.END, line + '\n', 'styleText')


def addScreen() :
    def checkTextBoxData() :
        if(accountNamePrompt.get() != '' and passwordPrompt.get() != '') :
            promptLabel2.configure(text='Information added Succesfully', fg='lime')
            aName = accountNamePrompt.get()
            aPassword = passwordPrompt.get()
            add(aName, aPassword)
            accountNamePrompt.delete(0, tk.END)
            accountNamePrompt.insert(0, "")
            passwordPrompt.delete(0, tk.END)
            passwordPrompt.insert(0, "")
        else :
            promptLabel2.configure(text="Please enter valid account name and password", fg="red")

    for widget in root.winfo_children() :
        widget.destroy()

    accountNameLabel = tk.Label(root, bg="black", fg="white", text="    Account Name :", font=("Consolas", 17, "bold"))
    accountNameLabel.place(relx=0.2, rely=0.2, anchor=tk.CENTER)

    accountNamePrompt = tk.Entry(root, width=30)
    accountNamePrompt.place(relx=0.7, rely=0.2, anchor=tk.CENTER)

    passwordLabel = tk.Label(root, bg="black", fg="white", text="        Password :", font=("Consolas", 17, "bold"))
    passwordLabel.place(relx=0.2, rely=0.4, anchor=tk.CENTER)

    passwordPrompt = tk.Entry(root, width=30)
    passwordPrompt.place(relx=0.7, rely=0.4, anchor=tk.CENTER)

    promptLabel2 = tk.Label(root, text="", bg="black", fg="lime", font=('Consolas', 13, 'italic'))
    promptLabel2.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    submitButton = tk.Button(root, text="Save", width="8", height="2", font=("Consolas", 18), fg="white", bg="#2D2826", command=checkTextBoxData)
    submitButton.place(relx=0.7, rely=0.8, anchor=tk.CENTER)

    backButton = tk.Button(root, text="Back", width="8", height="2", font=("Consolas", 18), fg="white", bg="#2D2826", command=managerScreen)
    backButton.place(relx=0.3, rely=0.8, anchor=tk.CENTER)


def managerScreen() :
    def checkPassword() :
        if masterPasswordPrompt.get() == masterPwd :
            viewScreen()
        else :
            promptLabel1.configure(text='Pleas enter correct master password', fg='red')

    for widget in root.winfo_children() :
        widget.destroy()

    headingLabel = tk.Label(root, text="Password Manager", bg="white", font=("Consolas", 25, "bold"), width=29)
    headingLabel.pack(pady=13)

    mainContentLabel = tk.Label(root, bg="#5F5E5D", width=72, height=14)
    mainContentLabel.pack(pady=10)

    promptLabel1 = tk.Label(mainContentLabel, text="", bg="#5F5E5D", fg="red", font=('Consolas', 13, 'italic'))
    promptLabel1.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    masterPasswordLabel = tk.Label(mainContentLabel, bg="#5F5E5D", fg="black", text="    Master Password :", font=("Consolas", 18, "bold"))
    masterPasswordLabel.place(relx=0.2, rely=0.2, anchor=tk.CENTER)

    masterPasswordPrompt = tk.Entry(mainContentLabel, width=30)
    masterPasswordPrompt.place(relx=0.7, rely=0.2, anchor=tk.CENTER)

    viewPasswordButton = tk.Button(mainContentLabel, text="View", width="8", height="2", font=("Consolas", 18), fg="white", bg="#2D2826", command=checkPassword)
    viewPasswordButton.place(relx=0.3, rely=0.7, anchor=tk.CENTER)

    addPasswordButton = tk.Button(mainContentLabel, text="Add", width="8", height="2", font=("Consolas", 18), fg="white", bg="#2D2826", command=addScreen)
    addPasswordButton.place(relx=0.7, rely=0.7, anchor=tk.CENTER)


root = tk.Tk()
root.title("Password Manager")
root.geometry("620x340")
root.configure(bg="black")

managerScreen()

root.mainloop()