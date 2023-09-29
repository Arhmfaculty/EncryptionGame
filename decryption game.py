import random
import string
import tkinter as tk
import time
import threading

# Create an a window object

window = tk.Tk()
window.title('Cryptographers')
window.geometry('1366x845')
window.config(bg='cyan')

# creating and displaying a welcome text on the window
greetings = tk.Label(window, font=('Ravie', 36, 'bold'), text='🔐Decryption Game🔐', fg='red', bg='cyan')
greetings.place(relx=0.5, rely=0.1, anchor="center")
# creating a caution message to the user
caution = tk.Label(window, font=('Lucida Handwriting', 20, 'bold'),
                   text='Please play in large screen for better experience.',
                   bg='cyan', fg='blue')
caution.place(relx=0.5, rely=0.4, anchor='center')

# Create an empty list for the sentences and append new sentence to the list
sentence = []
sentence.append('Our project is Typing Speed Test')
sentence.append('Some people combine touch typing and hunt')
sentence.append('This eliminates frequent up and down motions')
sentence.append('Somehow I found myself admiring the man')
sentence.append('it was their impatience with this kind of hypocrisy')
sentence.append('We all think we are first class people')
sentence.append('Many touch typists also use keyboard shortcuts')
sentence.append('Many experienced typist can type without looking at the keyboard')
sentence.append('This game is just for fun')

# creating an input area for typing
input_area = tk.Text(window, font=('ariel', 13), bg='white')
# create a global done button to be used anywhere in the code
global done_btn

# chose a random sentence from the list of sentences
passage = sentence[random.randint(0, len(sentence))]
ourWords = passage.split()
errors = []

key = []
alphabet = string.ascii_lowercase
for i in range(len(alphabet) - 1):
    key.append(i)
shift = random.randint(0, len(key))  # To randomly select a key for the user

shifted = alphabet[shift:] + alphabet[:shift] # to encrypt the sentence by starting from the particular key number
table = str.maketrans(alphabet, shifted)  # to map the alphabet to it corresponding shift
plainText = passage.lower()
cipherText = plainText.translate(table)

global error
global display


def checkResults():
    errors = []
    # TO ALLOW THEM TO DISAPPEAR WHEN THE DONE BUTTON IS CLICKED
    done_btn.pack()
    done_btn.pack_forget()
    displayText.pack()
    displayText.pack_forget()
    input_area.pack()
    input_area.pack_forget()
    alpha.pack()
    alpha.pack_forget()
    key.pack()
    key.pack_forget()
    keybtn.pack()
    keybtn.pack_forget()

    # to get the sentences from the user
    user_sentence = f"{input_area.get('1.0', 'end-1c')}"
    userWords = user_sentence.split()

    if len(userWords) == len(ourWords):
        for word in userWords:
            if word not in ourWords:
                errors.append(word)
        if len(errors) == 0:
            error1.place(relx=0.5, rely=0.2, anchor='center')
        else:
            error2 = tk.Label(window, text=f' Your wrong words are{errors}', font=('ariel', 15, 'bold'), bg='cyan',
                             fg='red')
            error2.place(relx=0.5, rely=0.2, anchor='center')
            display.place(relx=0.5, rely=0.5, anchor='center')
    elif len(userWords) < len(ourWords):
        error3.place(relx=0.5, rely=0.2, anchor='center')
        display.place(relx=0.5, rely=0.5, anchor='center')
        for word in userWords:
            if word not in ourWords:
                errors.append(word)
        if len(errors) == 0:
            error4.place(relx=0.5, rely=0.3, anchor='center')
            display.place(relx=0.5, rely=0.5, anchor='center')
        else:
            error5.place(relx=0.5, rely=0.3, anchor='center')
            display.place(relx=0.5, rely=0.5, anchor='center')
    else:
        error6.place(relx=0.5, rely=0.2, anchor='center')
        display.place(relx=0.5, rely=0.5, anchor='center')

        for word in ourWords:
            if word not in userWords:
                errors.append(word)
        if len(errors) == 0:

            error7.place(relx=0.5, rely=0.3, anchor='center')
        else:

            error8.place(relx=0.5, rely=0.3, anchor='center')
    Restartbtn.place(relx=0.5, rely=0.8, anchor='center')

def show_time():
    timer = tk.Text(window, width=5, height=1.5, fg='black', font=50, bg='white')
    timer.insert(tk.INSERT, "00:00")
    timer.place(relx=0.9, rely=0.05)
    start = time.time()
    seconds = 10
    while True:
        # allow timer to decrement
        if time.time() - start >= 1:
            seconds -= int(time.time() - start)
            start = time.time()
            cur_index = timer.index(tk.INSERT)
            cur_index = str(int(cur_index[0]) - 1) + cur_index[1:]
            timer.delete(cur_index, tk.INSERT)
            timer.insert(tk.INSERT, str(int(seconds / 60)) + ":" + str(seconds % 60))
            window.update()

        elif seconds == 0:
            # allow the program to automatically stops and submit the work when the timer reaches zero
            done_btn.pack()
            done_btn.pack_forget()
            displayText.pack()
            displayText.pack_forget()
            input_area.pack()
            input_area.pack_forget()
            alpha.pack()
            alpha.pack_forget()
            key.pack()
            key.pack_forget()
            checkResults()
            break
        # clear the start button, and the other messages when the start button is clicked
        start_btn.pack()
        start_btn.pack_forget()
        greetings.pack()
        greetings.pack_forget()
        caution.pack()
        caution.pack_forget()
        yesButton.pack()
        yesButton.pack_forget()
        noButton.pack()
        noButton.pack_forget()
        introLabel.pack()
        introLabel.pack_forget()

        # Allow the input area and the encrypted messages to be placed on the screen

        input_area.place(relx=0.5, rely=0.6, height=200, width=600, anchor='center')
        displayText.place(relx=0.5, rely=0.1, anchor='center')
        alpha.place(relx=0.5, rely=0.3, anchor='center')
        key.place(relx=0.5, rely=0.35, anchor='center')
        done_btn.place(relx=0.5, rely=0.8, anchor='center')
        keybtn.place(relx=0.2, rely=0.3)

        # to focus the cursor in the text box area
        input_area.focus()


def intorWindow():

    introLabel.place(relx=0.5, rely=0.2, anchor='center')
    yesButton.place(relx=0.45, rely=0.5, anchor='center')
    noButton.place(relx=0.55, rely=0.5, anchor='center')

    Restartbtn.pack()
    Restartbtn.pack_forget()
    error1.pack()
    error1.pack_forget()
    error2.pack()
    error2.pack_forget()
    error3.pack()
    error3.pack_forget()
    error4.pack()
    error4.pack_forget()
    error5.pack()
    error5.pack_forget()
    error6.pack()
    error6.pack_forget()
    error7.pack()
    error7.pack_forget()
    error8.pack()
    error8.pack_forget()
    display.pack()
    display.pack_forget()


displayText = tk.Label(window, font=('High Tower Text', 24, 'bold'), text=cipherText, wraplength=1360, fg='blue',
                       bg='cyan')
alpha = tk.Button(window, font=('Courier New', 20, 'bold'), text=alphabet.lower(), fg='black', bg='yellow')
key = tk.Button(window, font=('Courier New', 20, 'bold'), text=shifted.lower(), fg='white', bg='purple')
start_btn = tk.Button(window, text='Start👍', bg='yellow', fg='black', font=('Magneto', 20),
                      command=threading.Thread(target=show_time).start)
start_btn.place(relx=0.5, rely=0.8, anchor='center')
done_btn = tk.Button(window, text='Done👍', font=('ariel', 20, 'bold'), fg='black', bg='yellow',
                     command=lambda: checkResults())
keybtn = tk.Button(window, text='Keys >>>', font=('Ravie', 15, 'bold'), bg='magenta', fg='white')
Restartbtn = tk.Button(window, text='Restart', font=('Magneto', 18, 'bold'), bg='yellow', fg='black',
                       command=lambda: intorWindow())
introLabel = tk.Label(window, text="Do you want to play again?", font=('Lucida Handwriting', 20, 'bold'), bg='cyan',
                          fg='blue')
yesButton = tk.Button(window, text='  Yes👍', font=('magneto', 20, 'bold'), fg='black', bg='yellow',
                          command=threading.Thread(target=show_time).start)
noButton = tk.Button(window, text='No👎', font=('magneto', 20, 'bold'), fg='black', bg='yellow')
error1 = tk.Label(window, text='No wrong words', font=('ariel', 15, 'bold'), bg='cyan', fg='red')
error2 = tk.Label(window, text=f' Your wrong words are{errors}', font=('ariel', 15, 'bold'), bg='cyan',
                             fg='red')
display = tk.Label(window, text=f'THE RIGHT SENTENCE : {plainText}', font=('ariel', 18, 'bold'), fg='black',
                               bg='cyan')
error3 = tk.Label(window, text="You didn't type all words", font=('ariel', 15, 'bold'), bg='cyan', fg='red')
error4 = tk.Label(window, text='There is no wrong words for what you typed', font=('ariel', 15, 'bold'),
                         bg='cyan', fg='red')
error5 = tk.Label(window, text=f' Your wrong words are{errors}', font=('ariel', 15, 'bold'), bg='cyan',
                             fg='red')
error6 = tk.Label(window, text='You typed more words than expected', font=('ariel', 15, 'bold'), bg='cyan',
                         fg='red')
error7 = tk.Label(window, text='Congrats🎉🎉🥳🥳🥳🥳🥳'
                               'You typed all words right', font=('ariel', 15, 'bold'), bg='cyan', fg='red')
error8 = tk.Label(window, text=f' Your wrong words are {errors}', font=('ariel', 15, 'bold'), bg='cyan',
                             fg='red')

# TO ALLOW THE WINDOW TO STAY AWAKE WHILES THE PROGRAM IS STILL RUNNING
window.mainloop()








