"""
Student: Owen Pan
Student #: 722682
Teacher: Mr. Ghorvei
Due Date: June 22nd, 2021
Program: RetroCinemas Ticket Purchasing GUI Application
Assignment Description: Create a program based off SDLC that allows people to order movie tickets

Notes: I kept some of the code I used to navigate pages and debug as comments just in case there are future
bugs. I can just uncomment the pieces of code to check (these pieces of code are labeled)

Vocabulary - Widgets just refer those objects in tkinter such as labels, buttons, etc
"""

# imports all tkinter exposed objects in tkinter
from tkinter import *

# imports os module
import os


# This function takes the parameter, which is a frame (page) and shows the frame by bringing it up to the top
def show_frame(frame):
    frame.tkraise()   # tkraise() function raises the frame to the top, displaying it for the user


"""
_________________________________________________________________________________________________
"""


def checkout_process():  # this function is responsible for checkout, so anything after we click checkout button

    # creates the variable empty_fields which will be initialized to a label that says "Blank fields"
    global empty_fields

    # if there is a previous empty field, I want to destroy it since I don't want it to appear even when
    # the field are filled
    try:
        empty_fields.destroy()
    except:
        print()

    # we get the string for the entry into card number entry box during ticket purcahse
    cardNumber = cardNumberEntry.get()
    # we get the string for the entry into card name entry box during ticket purchase
    cardName = nameCardEntry.get()

    # print(cardNumberEntry.get())   <---- used previously to debug errors
    # print(nameCardEntry.get())     <----

    # the following will clear the entry boxes when we click checkout
    cardNumberEntry.delete(0,END)   # deletes entire string of current entry in cardNumberEntry widget
    nameCardEntry.delete(0,END)     # delete entire string of current entry in nameCardEntry widget

    # checks if the entries are empty, if they are not empty, checkout process will go through
    if cardNumber != "" and cardName !="":

        # subtracts seats from the array index corresponding the movie and time selection
        seats[movieNum-1][timeNum-1] -= ticketBuy

        # brings up the payment_info frame (aka the final checkout frame, after checkout is clicked)
        show_frame(f_payment_info)

        # set the price of the tickets to $10 per ticket
        price = float(ticketBuy)*10.00

        # print out to receipt as a label
        receipt = Label(f_payment_info, text = "RECEIPT\nLocation: RetroCinemas, Mississauga \n Tickets: x" + str(ticketBuy) + "\n Time: " + time + "\n Price: $" + str(price) +"0", font=("Courier", 15))
        receipt.place(x=500,y=200)

        # confirmation that order is successful, thank you message
        finish = Label(f_payment_info, text = "Your order has been successfully processed. \n Thank you and have a nice day!", font=("Courier", 20))
        finish.place(x=450,y=350)

        # displays a back to main menu button
        Button(f_payment_info,text="Return to Main Menu",command=lambda: show_frame(f_main)).place(x=900,y=500)

    else: # runs if the card number and card name entry are empty

        # displays a label telling the user that the fields are empty
        empty_fields=Label(f_ticket_purchase,text="Empty Fields", bg="red",fg="white")
        empty_fields.place(x=1050,y=410)

        # print("working") <---- previously used for debugging error


"""
_______________________________________________________________________________________
"""


def seat_availability():  # this function runs after seat availability button is clicked

    # time variable is created as a global variable, and initialized as the time the user selected
    global time
    time = clickedTime.get()

    # ticketBuy variable is created as a global variable, used to store number of tickets user buys
    global ticketBuy

    # checks if the user has selected the number of tickets he/she wants to buy, instead of leaving it as default
    try:
        # if the user has selected tickets, sets ticketBuy to clickedTickets (the number of tickets clicked
        # from the dropdown menu in ticket purchase frame)
        ticketBuy = int(clickedTickets.get())
    except:
        # if the user hasn't selected number of tickets, it sets ticket to 0, which will be processed by the
        # computer later in this function (approx. line 109)
        ticketBuy = 0

    global timeNum    # creates the global variable called timeNum
    timeNum = int(0)  # initializes the variable as an integer, 0
    if time == "9 am":  # if they user has selected the 9 am option, changes to 1
        timeNum=int(1)
    elif time == "12 pm":  # if they user has selected the 12 pm option, changes to 2
        timeNum = int(2)
    elif time == "3 pm":   # if they user has selected the 3 pm option, changes to 3
        timeNum = int(3)
    elif time == "6 pm":   # if they user has selected the 6 pm option, changes to 4
        timeNum = int(4)
    elif time == "9 pm":   # if they user has selected the 9 pm option, changes to 5
        timeNum = int(5)

    if timeNum != 0 and ticketBuy > 0:  # check if the time and tickets has been selected, not left on default
        # sets the number of tickets available to the corresponding indices in the 2d array
        # the 2d is organized by rows which represent the movies and columns which represent the times
        tickets = seats[movieNum-1][timeNum-1]
        # checks if there is enough tickets left for the user to by the selected amount
        if tickets-ticketBuy > 0:
            # shows how many seats are available for the current seating
            av = Label(f_ticket_purchase,text="There are "+str(tickets)+" available for this seating", bg="yellow",fg="blue")

            # creates global variable card number entry, allows user to enter card number
            global cardNumberEntry
            cardNumberEntry = Entry(f_ticket_purchase)
            cardNumberEntry.place(x=900, y=400)
            # creates label which tells user that the entry is for card number
            Label(f_ticket_purchase, text="Card Number").place(x=800, y=400)

            # create global variable for entry of name on card
            global nameCardEntry
            nameCardEntry = Entry(f_ticket_purchase)
            nameCardEntry.place(x=900, y=420)
            # creates label which tells user that the entry is for name on card
            Label(f_ticket_purchase, text="Name on Card").place(x=800, y=420)

            # sets the price for $10/ticket
            price = float(ticketBuy) * 10.00
            # displays the total cost to the user for their current selection
            Label(f_ticket_purchase, text="The total cost is $" + str(price) + "0").place(x=800, y=350)
            # displays a checkout option that allows the users to checkout, when pressed this button runs the
            # checkout_process() function which is located approx. line 27
            Button(f_ticket_purchase, text="CHECKOUT", fg="white", bg="red", command=lambda: checkout_process()).place(
                x=820, y=470)
        else:  # if the there are not enough seats to accommodate for the user's current selection
            # creates a label telling the user there are not enough seats left for their order, the user
            # can change their movie/time/(number of tickets)
            av = Label(f_ticket_purchase,text="There are not enough seats", bg="yellow",fg="blue")
    else: # if the card number entry or card name entry is empty
        # creates a label telling the user that they left a selection empty
        av = Label(f_ticket_purchase,text="Empty Selection", bg="yellow",fg="blue")

    # places the label created above
    av.place(x=920,y=200)


"""
_________________________________________________________________________________________
"""


# this function is responsible for displaying and images of the movie selected during movie selection and
# sets each movie to a corresponding number from 1-5
def ticket_movie_image(movieSelect):
    global movieNum   # creates global variable movieNum
    movieNum = int(0)  # initializes to 0
    if movieSelect==movie1Images:  # sets movie1 to 1
        movieNum=1
    elif movieSelect==movie2Images:  # sets movie1 to 2
        movieNum=2
    elif movieSelect==movie3Images:  # sets movie1 to 3
        movieNum=3
    elif movieSelect==movie4Images:  # sets movie1 to 4
        movieNum=4
    else:
        movieNum=5  # sets movie1 to 5

    # print(movieNum) <---- used previously for debugging errors

    # displays  the images of the movie in the ticket purchase and checkout frames
    Label(f_ticket_purchase, image=movieSelect, width=195,height=256).place(x=150,y=200)
    Label(f_payment_info, image=movieSelect, width=195,height=256).place(x=150,y=200)

    # displays the ticket purchasing frame
    show_frame(f_ticket_purchase)


"""
_________________________________________________________________________________________
"""


# this function takes username and password as parameters and checks them to see if they are in database(text files)
def login_verification(username, password):
    # defining global variables later used to label incorrect username or password
    global incorrect_password
    global incorrect_username

    # deletes previous iterations of label incorrect username or password, for example
    # if I had previously a wrong username, but I corrected it, I don't want it to still show wrong username
    try:
        incorrect_username.destroy()  # if this error exists from before, destroy it
        incorrect_password.destroy()  # if this error exists from before, destroy it
    except:
        try:
            incorrect_password.destroy()  # in the case that username was previously correct and password previously
        except:                           # correct but now the username is wrong
            print()
    finally:    # now that we deleted previous errors, we can check if current username as password is correct
        usernameInfo=username.get()  # set usernameInfo to the entry input into username
        passwordInfo=password.get()  # set passwordInfo to the entry input into password

        # list_of_files created and set to represent all file names in the current directory
        list_of_files = os.listdir()

        # checks for file titled with the username of user(I set the username to the file name during registration)
        if usernameInfo in list_of_files:
            # opens in read mode (if valid username)
            file1 = open(usernameInfo, "r")
            # read each line, splitting the read input where there is a new line
            verify = file1.read().splitlines()
            # checks if the password is in the file of the username (pass is written into this file during registration)
            if passwordInfo in verify:
                # if so, user successfully logs in and is brought to main page
                show_frame(f_main)
            else: # if not the user is told that the password is incorrect

                # print("incorrect password") <--- previously used to debug error
                # creates and places a label on page telling the user the password is incorrect
                incorrect_password = Label(f_login, text="Incorrect Password", fg="white", bg="red")
                incorrect_password.place(x=50,y=450)
        # if not username is found matching the user's input
        else:
            # print("username not recognized")  <--- previously used to debug error
            # creates and places a label on page telling the user the username is incorrect
            incorrect_username = Label(f_login, text="Incorrect Username", fg="white", bg="red")
            incorrect_username.place(x=50,y=400)

    # clears the entry from the username and password entry widgets from index 0 to end, using delete() function
    usernameEntryLog.delete(0, END)
    passwordEntryLog.delete(0, END)
    # allows us to enter a fresh username and password


"""
_________________________________________________________________________________________________
"""


# this function is used for registration verification
def register_verification(email, username, password, confirm_password):  # function takes in email, username,
                                                                         # password and confirm password as param.
    # sets global variables for each of the errors that will pop up as labels
    global blank_entry
    global username_taken
    global email_taken
    global password_not_match

    # if there is a previous error left from previous iteration, it tries to remove the label
    # This is similar to what happens in login
    # if a mistakes is made but correct, don't want error to still appear, that's why we destroy it
    try:
        blank_entry.destroy()
    except:
        print()
    try:
        email_taken.destroy()
    except:
        print()
    try:
        username_taken.destroy()
    except:
        print()
    try:
        password_not_match.destroy()
    except:
        print()

    # sets the following variables to the strings entered by the user for the various fields
    emailInfo=email.get()
    usernameInfo=username.get()
    passwordInfo=password.get()
    confirmPasswordInfo=confirm_password.get()

    # checks if any of the pieces of info are blank
    if emailInfo != "" and usernameInfo != "" and passwordInfo != "" and confirmPasswordInfo != "":
        # if they aren't blank, then we can do some more checking
        list_of_files = os.listdir() # list of files is the names of all files in directory
        # if we find that there is already a username of the same name in files, means username is already taken
        if usernameInfo in list_of_files:
            # creates a label telling the user that the username is taken
            username_taken = Label(f_register, text="Username Taken", fg="white", bg="red")
            username_taken.place(x=800, y=310)
        # if we find that there is already an email of the same name in files, means email is taken
        elif emailInfo in list_of_files:
            # creates a label telling the user that the email is taken
            email_taken = Label(f_register, text="Email Taken", fg="white", bg="red")
            email_taken.place(x=800, y=260)
        # if we find that the password entry does not match confirm password
        elif passwordInfo != confirmPasswordInfo:
            # creates a label telling the user that password does not match confirm password
            password_not_match = Label(f_register, text="Password does not match", fg="white", bg="red")
            password_not_match.place(x=800,y=385)
        else:  # if none of those problems occur, the user is successful in creating their account
            file = open(usernameInfo, "w")  # open a new file using the username
            file.write(usernameInfo + "\n")  # username is added into the file and split using a new line
            file.write(passwordInfo + "\n")  # password is added into file and split using a new line
            file2 = open(emailInfo, "w")     # a new file using the email is created
            file2.write(emailInfo)  # email is written into the file

            show_frame(f_main)  # shows the main frame (registration is done)
    else: # if any of the entry fields are empty
        # print("blank") <--- used previously for debugging
        # creates a label telling the user that there code contains a blank entry
        blank_entry = Label(f_register, text="Contains Blank Entries", fg="white", bg="red")
        blank_entry.place(x=800,y=210)

    # deletes the current entry in the entry boxes so user can enter fresh entry
    emailEntryReg.delete(0,END)
    usernameEntryReg.delete(0, END)
    passwordEntryReg.delete(0, END)
    confirmPasswordEntryReg.delete(0,END)


"""
_________________________________________________________________________________________________
"""


# This function creates the login screen, adding the initial widgets
def login_page():

    # colour-coded background used to distinguish pages during development
    Label(f_login, bg="blue").place(x=0, y=0, relwidth=1, relheight=1)

    # create global variable bg, this will be initialized as a PhotoImage object with the background blue colour
    # all images have to use global if they are in function or they will appear as a blank
    global bg
    bg = PhotoImage(file="Image/background.png")
    # the blue background colour is placed
    Label(f_login, image=bg, width=1200, height=600).place(x=-2, y=0)

    # creates title variable that holds the title images
    global title
    title = PhotoImage(file="Image/title (1).png")
    # places the image as a label
    Label(f_login, image=title,width=260,height=90).place(x=470, y=100)

    # create loginImage variable that hold the login image
    global loginImage
    loginImage = PhotoImage(file="Image/login.png")
    # places the image as a label
    Label(f_login, image=loginImage,width=180, height=90).place(x=250, y=280)

    # creates registerImage variable that holds the registerImage
    global registerImage
    registerImage = PhotoImage(file="Image/register.png")
    # places the registerImage on a button, which leads to the register screen when clicked
    Button(f_login,image=registerImage, bg="yellow", command=lambda: show_frame(f_register)).place(x=750,y=320)

    # Username and password created a StringVar()
    # StringVar is a class helps access and interpret information, we use StringVar to access the input
    # of the user into our entry widgets.
    username = StringVar()
    password = StringVar()

    # creates usernameImage variable that hold usernameImage
    global usernameImage
    usernameImage = PhotoImage(file="Image/username.png")
    # places usernameImage using label
    Label(f_login, image=usernameImage,width=122,height=28).place(x=170, y=389)

    # creates usernameEntryLog which is initialized as an Entry widget
    global usernameEntryLog
    usernameEntryLog = Entry(f_login, textvariable=username)  # the user input is stored as username
    # entry widget is placed
    usernameEntryLog.place(x=330, y=400)

    # creates passwordImage variable that hold an image
    global passwordImage
    passwordImage = PhotoImage(file="Image/password.png")
    # places the image using a label
    Label(f_login, image=passwordImage,width=126,height=28).place(x=170, y=439)

    # creates passwordEntryLog which is initialized as an Entry widget
    global passwordEntryLog
    passwordEntryLog = Entry(f_login, textvariable=password)  # the user input is stored as password
    # entry widget is placed
    passwordEntryLog.place(x=330, y=450)

    # create orImage variable that stores an image
    global orImage
    orImage = PhotoImage(file="Image/or.png")
    # place images on screen using a label
    Label(f_login, image=orImage, width=90, height=63).place(x=550, y=350)

    # The following code is used previously during development for debugging errors and navigating pages
    """
    Label(f_login, text='Login Page').place(x=0, y=0)
    Button(f_login, text='Registration Page', command=lambda: show_frame(f_register)).place(x=0, y=30)
    Button(f_login, text='Main Page', command=lambda: show_frame(f_main)).place(x=100, y=30)
    """

    # creates arrowImage which stores image
    global arrowImage
    arrowImage = PhotoImage(file="Image/arrow.png")
    # places the image using a button, that when pressed runs the function login_verification, which takes
    # parameters of username and password
    Button(f_login, image=arrowImage, bg="yellow", command=lambda: login_verification(username, password)).place(x=350, y=500)


"""
_________________________________________________________________________________________________
"""


# this function creates base of the register pages, adds basic widgets to the registration page
def register_page():
    # fills in background purple (colour coding was initially used to distinguish each page)
    Label(f_register, bg="purple").place(x=0, y=0, relwidth=1, relheight=1)
    # fills background with a blue colour
    Label(f_register, image=bg, width=1200, height=600).place(x=-2, y=0)
    # displays the register image
    Label(f_register, image=registerImage, width=283, height=92).place(x=470, y=100)

    # displays and place email label which is beside email entry
    global emailImage
    emailImage=PhotoImage(file="Image/email.png")
    Label(f_register, image=emailImage, width=65, height=28).place(x=455, y=250)

    # displays and places username label which is beside username entry
    Label(f_register, image=usernameImage, width=122, height=28).place(x=400, y=300)

    # displays and places password label which is beside password entry
    Label(f_register, image=passwordImage, width=126, height=28).place(x=400, y=350)

    # displays and places confirm password label which is beside confirm password entry
    global confirmPassImage
    confirmPassImage = PhotoImage(file="Image/confirm password.png")
    Label(f_register, image=confirmPassImage, width=70, height=28).place(x=453, y=400)

    # create variables and sets them to StringVar() so we can store the entries made by users in entry widgets
    email = StringVar()
    username = StringVar()
    password = StringVar()
    confirmPassword = StringVar()

    # creates entry widget so user can enter email
    global emailEntryReg
    emailEntryReg = Entry(f_register, textvariable=email)  # takes the entry as a textvariable saved to email
    # places the entry widget
    emailEntryReg.place(x=580, y=260)

    # creates entry widget so user can enter username
    global usernameEntryReg
    usernameEntryReg= Entry(f_register, textvariable=username)  # takes the entry as a textvariable saved to username
    # places the entry widget
    usernameEntryReg.place(x=580, y=310)

    # creates entry widget so user can enter password
    global passwordEntryReg
    passwordEntryReg = Entry(f_register, textvariable=password)  # takes the entry as a textvariable saved to password
    # places the entry widget
    passwordEntryReg.place(x=580, y=360)

    # creates entry widget so user can enter password again
    global confirmPasswordEntryReg
    confirmPasswordEntryReg = Entry(f_register, textvariable=confirmPassword)   # takes the entry as a textvariable saves it to confirm password
    # places the entry widget
    confirmPasswordEntryReg.place(x=580, y=410)

    # creates and places a button that allows the user to register, when clicked, runs register_verification function
    Button(f_register, image=arrowImage, bg="yellow", command=lambda: register_verification(email,username, password, confirmPassword)).place(x=580, y= 460)

    # creates and places a button that is displayed with an image, when clicked, the button goes to previous page
    global backarrowImage
    backarrowImage = PhotoImage(file="Image/backarrow.png")
    # when clicked, the button runs show_frame function, which displays the frame put into parameter
    # in this case, it will display the login screen
    Button(f_register, image=backarrowImage, width=37, height=20,command=lambda: show_frame(f_login)).place(x=50, y=50)

    # The following code is used previously during development for debugging errors and navigating pages
    """
    Label(f_register, text='Registration Page').place(x=0, y=0)
    Button(f_register, text='Main Page', command=lambda: show_frame(f_main)).place(x=0, y=30)
    """


"""
_________________________________________________________________________________________________
"""


# this function loads the main screen with the initial widgets
def main_page():
    # colour-coded background used during development to differentiate between pages
    Label(f_main, bg="yellow").place(x=0, y=0, relwidth=1, relheight=1)
    # new blue background is placed over yellow-background
    Label(f_main, image=bg, width=1200, height=600).place(x=-2, y=0)

    # the title image (RetroCinemas) is placed onto the main page
    Label(f_main, image=title, width=260, height=90).place(x=470, y=100)

    # the first movie image is created and placed onto the frame
    global movie1Images
    movie1Images = PhotoImage(file="Image/movie1.png")
    Label(f_main, image=movie1Images, width=195, height=259).place(x=510, y=200)

    # the second movie image is created and placed onto the frame
    global movie2Images
    movie2Images = PhotoImage(file="Image/movie2.png")
    Label(f_main, image=movie2Images, width=195, height=259).place(x=268, y=310)

    # the third movie image is created and placed onto the frame
    global movie3Images
    movie3Images = PhotoImage(file="Image/movie3.png")
    Label(f_main, image=movie3Images, width=195, height=259).place(x=30, y=200)

    # the fourth movie image is created and placed onto the frame
    global movie4Images
    movie4Images = PhotoImage(file="Image/movie4.png")
    Label(f_main, image=movie4Images, width=195, height=259).place(x=751, y=310)

    # the fifth movie image is created and placed onto the frame
    global movie5Images
    movie5Images = PhotoImage(file="Image/movie5.png")
    Label(f_main, image=movie5Images, width=195, height=256).place(x=980, y=200)

    # the now playing button is created and placed onto the frame
    global nowplayingImage
    nowplayingImage = PhotoImage(file="Image/nowplaying.png")
    # when the button is clicked, it runs the function show_frame() taking in the movie selection frame
    # this will display the movie select frame, which allows user to buy movie tickets
    Button(f_main, bg="yellow", image=nowplayingImage, width=185, height=29,command=lambda: show_frame(f_movie_select)).place(x=515, y=500)

    # The following code is used previously during development for debugging errors and navigating pages
    """
    Label(f_main, text='Main Page').place(x=0, y=0)
    Button(f_main, text='Movie Page', command=lambda: show_frame(f_movie_select)).place(x=0, y=30)
    """

"""
_________________________________________________________________________________________________
"""


# this function creates the initial movie selection page where the user can select the movie
def movie_page():
    # colour-coded background used during development to differentiate between pages
    Label(f_movie_select, bg="red").place(x=0, y=0, relwidth=1, relheight=1)
    # new blue coloured background is placed over colour-coded background
    Label(f_movie_select, image=bg, width=1200, height=600).place(x=-2, y=0)

# the following image variable have already been created and set previously as global variables, so we can use
# them again without have to create new PhotoImage objects
    # places title on screen
    Label(f_movie_select, image=title, width=260, height=90).place(x=470, y=100)
    # places 1st movie image on screen
    Label(f_movie_select, image=movie1Images, width=195, height=259).place(x=510, y=200)
    # places 2nd movie on screen
    Label(f_movie_select, image=movie2Images, width=195, height=259).place(x=268, y=310)
    # places 3rd movie on screen
    Label(f_movie_select, image=movie3Images, width=195, height=259).place(x=30, y=200)
    # places 4th movie on screen
    Label(f_movie_select, image=movie4Images, width=195, height=259).place(x=751, y=310)
    # places 5th movie on screen
    Label(f_movie_select, image=movie5Images, width=195, height=256).place(x=980, y=200)

    # select movie label is created and placed onto the page
    global selectmovieImage
    selectmovieImage = PhotoImage(file="Image/selectmovie.png")
    Label(f_movie_select, bg="yellow", image=selectmovieImage, width=185, height=70).place(x=515, y=500)

    # the orderTicketImage is created to store the order button image
    global orderTicketImage
    orderTicketImage = PhotoImage(file="Image/button.png")
    # 5 Buttons are created, each for their respective movies
    # each button will issue the command to run ticket_movie_image function, which takes in a PhotoImage parameter
    # each button will give different PhotoImage objects which will be displayed on later pages
    Button(f_movie_select, bg="yellow", image=orderTicketImage, width=28, height=20, command=lambda: ticket_movie_image(movie1Images)).place(x=510, y=200)
    Button(f_movie_select, bg="yellow", image=orderTicketImage, width=28, height=20, command=lambda: ticket_movie_image(movie2Images)).place(x=268, y=310)
    Button(f_movie_select, bg="yellow", image=orderTicketImage, width=28, height=20, command=lambda: ticket_movie_image(movie3Images)).place(x=30, y=200)
    Button(f_movie_select, bg="yellow", image=orderTicketImage, width=28, height=20, command=lambda: ticket_movie_image(movie4Images)).place(x=751, y=310)
    Button(f_movie_select, bg="yellow", image=orderTicketImage, width=28, height=20, command=lambda: ticket_movie_image(movie5Images)).place(x=980, y=200)

    # The following code is used previously during development for debugging errors and navigating pages
    """
    Label(f_movie_select, text='Movie Page').place(x=0, y=0)
    Button(f_movie_select, text='Back to Main Page', command=lambda: show_frame(f_main)).place(x=0, y=30)
    Button(f_movie_select, text='Ticket page', command=lambda: show_frame(f_ticket_purchase)).place(x=150, y=30)
    """

    # this button allows the user to go back to the previous screen, show_frame function runs which f_main, this
    # tells the program to show the main frame, which is the previous page
    Button(f_movie_select, image=backarrowImage, width=37, height=20, command=lambda: show_frame(f_main)).place(x=50, y=50)


"""
_________________________________________________________________________________________________
"""


# adds initial widgets onto the ticket page
def ticket_page():
    # colour-coded background used during development to differentiate between pages
    Label(f_ticket_purchase, bg="orange").place(x=0, y=0, relwidth=1, relheight=1)
    # new blue coloured background is placed over colour-coded background
    Label(f_ticket_purchase, image=bg, width=1200, height=600).place(x=-2, y=0)

    # create a global variable called clickedTime which is a StringVar()
    global clickedTime
    clickedTime = StringVar()
    # set clickTime to be initially set to --time--
    clickedTime.set("--Time--")

    # create a dropdown menu for the time of movie seating, the selection is stored as clickedTime
    time_drop = OptionMenu(f_ticket_purchase, clickedTime,"9 am", "12 pm", "3 pm", "6 pm", "9 pm")
    # places the drop down menu
    time_drop.place(x=450, y=200)

    # create a global variable called clickedTickets which is a StringVar()
    global clickedTickets
    clickedTickets = StringVar()
    # set clickTime to be initially set to --Number of Tickets--
    clickedTickets.set("--Number of Tickets--")

    # create a dropdown menu for the number of tickets the user can buy, the selection is recorded as clickedTickets
    ticket_drop = OptionMenu(f_ticket_purchase, clickedTickets, "1","2","3","4","5","6")
    # places the drop down menu
    ticket_drop.place(x=450, y=300)

    # creates and places the checkout image title
    global checkoutImage
    checkoutImage = PhotoImage(file="Image/checkout.png")
    Label(f_ticket_purchase, image=checkoutImage, width=235,height=83).place(x=240,y=80)

    # creates a button that checks for availability of the selection, runs command seat_available to check
    Button(f_ticket_purchase, text="Check for Seat Availability",bg="yellow",fg="blue",command=lambda: seat_availability()).place(x=650,y=200)

    # The following code is used previously during development for debugging errors and navigating pages
    """
    Label(f_ticket_purchase, text='Ticket Page').place(x=0, y=0)
    Button(f_ticket_purchase, text='Back to Main Page', command=lambda: show_frame(f_main)).place(x=0, y=30)
    Button(f_ticket_purchase, text='Purchase Page', command=lambda: show_frame(f_payment_info)).place(x=150, y=30)
    """

    # this button allows the user to go back to the previous screen, show_frame function runs which f_main, this
    # tells the program to show the movie select frame, which is the previous page
    Button(f_ticket_purchase, image=backarrowImage, width=37, height=20, command=lambda: show_frame(f_movie_select)).place(x=50, y=50)


"""
_________________________________________________________________________________________________
"""


# adds initial widgets to the payment page
def payment_page():
    # colour-coded background used during development to differentiate between pages
    Label(f_payment_info, bg="green").place(x=0, y=0, relwidth=1, relheight=1)
    # new blue coloured background is placed over colour-coded background
    Label(f_payment_info, image=bg, width=1200, height=600).place(x=-2, y=0)

    # The following code is used previously during development for debugging errors and navigating pages
    """
    Label(f_payment_info, text='Payment Page').place(x=0, y=0)
    Button(f_payment_info, text='Back to Main Page', command=lambda: show_frame(f_main)).place(x=0, y=30)
    """

    # adds checkoutImage as a label, it was created in ticket purchase function as a global variable
    # thus, we don't have to create it again
    Label(f_payment_info, image=checkoutImage, width=235, height=83).place(x=240, y=80)


"""
_________________________________________________________________________________________________
"""


# initializes tkinter, window with title bar where you can add widgets
root = Tk()

# sets a window size for the application
root.geometry("1200x600")

# sets title of window bar at top of window
root.title("RetroCinemas")

# array for seats
global seats
# initializes all the seats to have a maximum seating of 20 people (small movie theatre)
seats = [[20,20,20,20,20],[20,20,20,20,20],[20,20,20,20,20],[20,20,20,20,20],[20,20,20,20,20]]


# initializes all the pages of the application, adding each page to the root(window), each page is represented
# as a frame
f_main = Frame(root)
f_login = Frame(root)
f_register = Frame(root)
f_movie_select = Frame(root)
f_ticket_purchase = Frame(root)
f_payment_info = Frame(root)

# initializes all the frames, telling it to fill up the entire screen
# for loop iterates through all the frames listed, running the .place() function
for frame in (f_login, f_register, f_main, f_payment_info, f_movie_select, f_ticket_purchase):

    # necessary command to place (pack) the frame onto the window (root)
    # we want the put the frame and have it expand until it covers the entire window,
    # relwidth = 1 and relheight = 1 expands the frame to fit the window
    frame.place(x=0,y=0,relwidth=1, relheight=1)

"""
The following code below runs each of the functions that creates each page, decorating them with various
initial widgets that appear on screen. Widgets are items that can be added onto the page such as labels, 
buttons, etc... Basically, by running these functions, the program would have created and designed all the 
pages, at least initially (because the pages change). The reason I chose to make all the pages individual 
functions instead of on main code is for organization purposes. If I need to find an error relating to 
some faulty pages, I will know exactly where the code is.
"""
login_page()
register_page()
main_page()
movie_page()
ticket_page()
payment_page()

# I am putting the logout button on every single page except login and register pages
# creates logoutImage as a photo object that created the logout.png image
logoutImage = PhotoImage(file="Image/logout.png")
# iterates through each frame in the list to add the logout button
for frame in (f_main, f_payment_info, f_movie_select, f_ticket_purchase):
    Button(frame, image=logoutImage, bg="yellow", command=lambda: show_frame(f_login)).place(x=1060,y=5)

# starts the program by showing the login screen
show_frame(f_login)

# .mainloop() executes, loops code continuously so we can actually see a gui, and not have the program
# run though once and instantly abort
root.mainloop()
