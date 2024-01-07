import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import string as str
import secrets

 
# Συμβολοσειρές που περιέχουν όλους τους λατινικούς χαρακτήρες, τα νούμερα και τα σύμβολα
uppercase = str.ascii_uppercase
lowercase = str.ascii_lowercase
numbers = str.digits
symbols = str.punctuation


class Create_password():
    '''Κλάση δημιουργίας ισχυρών κωδικών'''
    def __init__(self, lower, upper, numbers, symbols):           
        self.lower = lower
        self.upper = upper
        self.numbers = numbers
        self.symbols = symbols


    # Έλεγχος των εισόδων του χρήστη (το συνολικό πλήθος χαρακτήρων πρέπει να έινα μεταξύ του 4 και του 40)
    def check_inputs(self):
        if self.upper+self.numbers+self.symbols+self.lower < 4:      
            tk.messagebox.showerror(title="Error", message="The Sum of numbers, symbols, uppercase and lowercase characters must be higher than 4")
            return False

        elif self.upper+self.numbers+self.symbols+self.lower > 40:
            tk.messagebox.showerror(title="Error", message="The Sum of numbers, symbols and uppercase can not exceed number 40")
            return False

        else:
            return True
        


    # Συνάρτηση δημιουργίας των κωδικών αξιοποιώντας τις παραπάνω συμβολοσειρές 
    def generate_password(self):
        self.check_inputs()                            # Καλούμε την check_inputs 
        
        password = []
        if self.check_inputs():                        # Αν η check_inputs επιστρέφει True, τότε δημιουργούμε τον κωδικό
            
            password += [secrets.choice(uppercase) for i in range(self.upper)]
            password += [secrets.choice(numbers) for i in range(self.numbers)]
            password += [secrets.choice(symbols) for i in range(self.symbols)]
            password += [secrets.choice(lowercase) for i in range(self.lower)]
            secrets.SystemRandom().shuffle(password)    # Ανακατεύουμε τη λίστα password για να είναι τυχαία η σειρά των χαρακτήρων  
            password = ''.join(password)                # Μετατρέπουμε τη λίστα σε συμβολοσειρά
        

        return password



class MyApp():
    '''Κλάση η οποία δημιουργεί το παράθυρο της εφαρμογής και τα 4 LabelFrame'''
    def __init__(self, w):

        # Δημιουργία του παραθύρου και widgets
        self.window = w
        self.window.title("Strong Password Generator")
        self.window.iconbitmap('lock_icon.ico')
        self.window.geometry('580x360')
        self.frame = tk.Frame(w, bg = "#E5E7E9")
        self.frame.pack()
        self.enter_pass_frame = tk.LabelFrame(self.frame, bg="#E5E7E9")
        self.enter_pass_frame.grid(row=1,column=0,ipadx=7,ipady=20)

        
        self.password_entry = tk.StringVar()
        vcmd = (w.register(self.validate_entries), '%S')


        self.lower_label = tk.Label(self.enter_pass_frame, text = "LowerCase", bg="#E5E7E9")
        self.lower_label.grid(row=0,column=0)
        self.lower_label_entry = tk.Entry(self.enter_pass_frame, validate="all", validatecommand=vcmd)
        self.lower_label_entry.grid(row=1,column=0)

        self.numbers_label = tk.Label(self.enter_pass_frame, text = "Numbers", bg="#E5E7E9")
        self.numbers_label.grid(row=0,column=1)
        self.numbers_label_entry = tk.Entry(self.enter_pass_frame, validate="all", validatecommand=vcmd)
        self.numbers_label_entry.grid(row=1,column=1)

        self.symbols_label = tk.Label(self.enter_pass_frame, text = "Symbols", bg="#E5E7E9")
        self.symbols_label.grid(row=0,column=2)
        self.symbols_label_entry = tk.Entry(self.enter_pass_frame, validate="all", validatecommand=vcmd)
        self.symbols_label_entry.grid(row=1,column=2)

        self.uppercase_label = tk.Label(self.enter_pass_frame, text = "UpperCase", bg="#E5E7E9")
        self.uppercase_label.grid(row=0,column=3)
        self.uppercase_label_entry = tk.Entry(self.enter_pass_frame, validate="all", validatecommand=vcmd)
        self.uppercase_label_entry.grid(row=1,column=3)

    
        # Προσδιορίζει τις αποστάσεις στο πρώτο LabelFrame,χωρίς να γίνονται ξεχωριστά για το κάθε widget(χρησιμοποιείτε για χάρη ευκολίας
        for widget in self.enter_pass_frame.winfo_children():
            widget.grid_configure(padx=5,pady=5)


        self.password_frame = tk.LabelFrame(self.frame, bg="#E5E7E9")
        self.password_frame.grid(row=2,column=0,sticky='news',padx=10,pady=20, ipady=10)

        self.mypass = tk.Entry(self.password_frame,text="",font=("Arial",12), width= 30, state = 'readonly', bd=2, show="", textvariable = self.password_entry)
        self.mypass.grid(row=0,column=1,padx=10)

        self.copy_button = tk.Button(self.password_frame,text ="Copy Password", command = self.copy, bg='#D7DBDD')
        self.copy_button.grid(row=0,column=3,)


        self.pass_label = tk.Label(self.password_frame, text = "The password is: ", bg="#E5E7E9")
        self.pass_label.grid(row=0,column=0)

        self.hide_button = tk.Checkbutton(self.password_frame, text = "Hide password", bg="#E5E7E9", command = self.show_password)
        self.hide_button.grid(row=1,column=0)



        self.button1 = tk.Button(self.enter_pass_frame, text = "Generate Password", font = ('Arial',10), command = self.start, bg='#D7DBDD', width=30)
        self.button1.place(x=143, y=60)



        self.password_generator = tk.LabelFrame(self.frame, width=500, height=75, bg='#B2BABB')
        self.password_generator.grid(row=0, column=0, padx=10)
        self.test = tk.Label(self.password_generator, text = "Strong Password Generator", font=('Helvetica',18), fg='#000000', bg='#B2BABB')
        self.test.grid(row=0, column=0, padx=122, pady=30)


        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

    # Κάλεσμα των συναρτήσεων start και copy, όταν πατηθούν τα enter και Control-c
        self.window.bind('<Return>', self.start)
        self.window.bind('<Control-c>', self.copy)
        self.window.bind('<Control-C>', self.copy)


    # Δημιουργία αντικειμένου passwords_manager της κλάσης Passwords_Manager 
        self.passwords_manager = Passwords_Manager(self.window, self.frame, self.password_frame, self.password_entry)

    # Συνάρτηση που ελέγχει αν η είσοδος του χρήστη αποτελείται μόνο από νούμερα
    def validate_entries(self, char):
        return char.isdigit()

    # Συνάρτηση η οποία είναι υπεύθυνη για την εκχώρηση σε μεταβλητές τις τιμές των εισόδων
    def take_entries(self):
        lower = self.lower_label_entry.get()
        upper = self.uppercase_label_entry.get()
        numbers = self.numbers_label_entry.get()
        symbols = self.symbols_label_entry.get()

        if lower == "":
            lower = 0
        if numbers == "":
            numbers = 0
        if symbols == "":
            symbols = 0
        if upper == "":
            upper = 0

        Create_password.lower = int(lower)
        Create_password.upper = int(upper)
        Create_password.numbers = int(numbers)
        Create_password.symbols = int(symbols)
        
    # Η συνάρτηση start προσδίδει λειτουργία στο Button Generate Password, έτσι ώστε να παράγει τυχαίους κωδικούς
    def start(self, e=None):
        self.take_entries()
        password = Create_password(Create_password.lower, Create_password.upper, Create_password.numbers, Create_password.symbols)

        self.mypass.configure(state = 'normal')
        self.mypass.delete(0, tk.END)
        self.mypass.insert(0,password.generate_password())
        self.mypass.configure(state = 'readonly')

    # Η συνάρτηση copy προσδίδει λειτουργία στο  Button Copy Password, έτσι ώστε να μπορεί να αποθηκεύει ο χρήστης τους επιθυμητούς κωδικούς
    def copy(self,e=None):
        self.window.clipboard_clear()
        self.window.clipboard_append(self.mypass.get())

    # Με την συνάρτηση show_passwords ο χρήστης μπορεί να αποκρύψει τον κωδικό του, καθώς προσδίδει τούτη την ιδιότητα στον Checkbutton και αυτό επιτυγχάνεται με το πάτημα του
    def show_password(self):
        if self.mypass.cget('show')== "":
            self.mypass.configure(show="*")
        else:
           self.mypass.configure(show="")    

    # Με την συνάρτηση on_close δημιουργείτε ένα popup text που ενημερώνει το χρήστη ότι έχει μη αποθηκευμένους κωδικούς και αν επιθυμεί να εξέλθει απο την εφαρμογή
    def on_close(self):
        current_password = self.mypass.get()
        with open("passwords.txt", "r") as file:
            passwords = file.readlines()
            passwords = "".join(passwords)
            if current_password in passwords:
                self.window.destroy()
            else:
                ans = tk.messagebox.askyesno(title="Exit?", message="There is unsaved password. Are you sure you want to exit without saving?")
                if ans:
                    self.window.destroy()               
            


class Passwords_Manager():
    '''Κλάση διαχείρησης των κωδικών'''
    def __init__(self, w, frame, password_frame, password):
        self.window = w
        self.frame = frame
        self.password_frame = password_frame
        self.password = password


        self.button2 = tk.Button(self.password_frame, text = "Save  Password", bg='#D7DBDD', command=self.save_window)
        self.button2.grid(row=1,column=3)


        self.button3 = tk.Button(self.frame, text = "Show Passwords", font = ('Arial',10), bg='#D7DBDD', command=self.display_saved_passwords)
        self.button3.grid(row=6,column=0,sticky='news',padx=5,pady=5)


        self.window.bind('<Control-s>', self.save_window)
        self.window.bind('<Control-S>', self.save_window)

    # Με τη συνάρτηση save_window δημιουργείται ένα καινούριο παράθυρο στο οποίο ο χρήστης πληκτρολογεί ένα keyword για τον κωδικό που θέλει να αποθηκεύσει
    def save_window(self, e=None):
        self.top = tk.Toplevel()
        self.top.geometry('350x75')
        self.top.title("Strong Password Generator")
        self.top.iconbitmap('lock_icon.ico')

        self.top.grab_set()

        self.save_frame = tk.Frame(self.top, bg = '#E5E7E9')
        self.save_frame.pack(fill='both', expand=1)
        
        self.save_label = tk.Label(self.save_frame, text = "Enter a keyword for your password:", bg = '#E5E7E9')
        self.save_label.place(x=5, y=20)

        self.save_entry = tk.Entry(self.save_frame)
        self.save_entry.place(x=200, y=20)

        self.save_button = tk.Button(self.save_frame, text = "Save", command = self.save_password, width = 10, bg='#D7DBDD')
        self.save_button.place(x=90, y = 45)

        self.cancel_button = tk.Button(self.save_frame, text = "Cancel", command = self.top.destroy, width = 10, bg='#D7DBDD')
        self.cancel_button.place(x=200, y = 45)

    # Η συνάρτηση save_password αποθηκεύει τους κωδικούς και ελέγχει αν έχουν διαφορετικό keyword δίνοντας error αν έχουν το ίδιο
    def save_password(self):
        
        password=self.password.get()
        keyword = self.save_entry.get()
        with open('passwords.txt','r') as file:
            passwords = file.readlines()
            passwords = "".join(passwords) 
        if keyword in passwords and keyword !="":
            tk.messagebox.showerror(title='Error', message=f'Error! Password with keyword {keyword} already exists!')
        elif keyword == "":
            pass
        else:           
            x = f'{keyword}: {password}'        
            with open('passwords.txt','a') as file:
                file.write(x+'\n') 
        
            self.top.destroy()
            tk.messagebox.showinfo(title="Password Saved", message = "Password Saved Succesfully!")


        
    # Η συνάρτηση display_sved_passwords ανοίγει ένα καινούριο παράθυρο στο οποίο φαίνονται οι αποθηκευμένοι κωδικοί τους οποίους τους διαβάζει από το αρχείο που είναι αποθηκευμένοι
    def display_saved_passwords(self):
        self.show_passwords = tk.Toplevel()
        self.show_passwords.geometry("580x450")
        self.show_passwords.title("Strong Password Generator")
        self.show_passwords.iconbitmap("lock_icon.ico")

        self.show_passwords.grab_set()


        self.show_passwords_frame = tk.Frame(self.show_passwords, bg = '#E5E7E9')
        self.show_passwords_frame.pack(fill="both", expand=1)

        # Scrollbar
        self.show_passwords_canvas = tk.Canvas(self.show_passwords_frame, bg = '#E5E7E9')
        self.show_passwords_canvas.pack(fill='both', expand=1, side='left')        

        scrollbar = ttk.Scrollbar(self.show_passwords_frame, orient="vertical", command=self.show_passwords_canvas.yview)
        scrollbar.pack(side='right', fill="y")

        self.show_passwords_canvas.configure(yscrollcommand=scrollbar.set)
        self.show_passwords_canvas.bind('<Configure>', lambda e:self.show_passwords_canvas.configure(scrollregion=self.show_passwords_canvas.bbox('all')))

        second_frame = tk.Frame(self.show_passwords_canvas, bg='#E5E7E9')


        self.show_passwords_canvas.create_window((0,0), window=second_frame)

        try:
            with open("passwords.txt", "r") as file:
                passwords = file.readlines()
                for i,password in enumerate(passwords, start = 1):
                    password_label = tk.Label(second_frame, text =f"{i}\t{password}", bg='#E5E7E9', font=16)
                    password_label.grid(row=i, column=0, sticky='w', padx=5, pady=2)
        except FileNotFoundError:
            tk.messagebox.showinfo(title="File Not Found", message='Error! File not found')
     


# Κυρίως πρόγραμμα
if __name__ == "__main__":
    w = tk.Tk()
    app = MyApp(w)
    w.mainloop()    