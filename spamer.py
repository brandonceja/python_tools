import pyautogui as autom
import tkinter

autom.FAIL_SAFE = True


def initializeWindow():
    root = tkinter.Tk()
    root.resizable(width=False, height=False)
    root.config(bg="black")
    root.geometry("310x100")
    root.title("Python Spammer")

    testLabel = tkinter.Label(root, text="Enter the string: ", font='Helvetica 11 bold',
                              pady=10, bg='black', fg='white')
    testLabel.grid(row=0, column=0)

    inputs = tkinter.Entry(root)
    inputs.config(bg='#D3D3D3')
    inputs.grid(row=0, column=1)

    btn1 = tkinter.Button(root, text="Start", width=16, font='Helvetica 9 bold',
                          bg='#126CFF', fg='white', highlightthickness=0)
    btn1.grid(row=1, column=0, padx=10)
    btn1.config(command=lambda: write(inputs.get()))

    btn2 = tkinter.Button(root, text="Stop", width=17, font='Helvetica 9 bold',
                          bg='#FC2E2E', fg='white', highlightthickness=0)
    btn2.grid(row=1, column=1)
    btn2.config(command=exit)

    root.mainloop()


def write(text):
    while True:
        autom.typewrite(text, 0)
        autom.typewrite(['enter'], 0)


initializeWindow()
