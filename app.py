from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NlpApp:
    def __init__(self):
        self.dbo=Database()
        self.apio=API()
        self.root =Tk()
        self.root.title('NLP')
        self.root.geometry('350x500')
        self.root.configure(bg='silver')

        self.login()


        self.root.mainloop()

    def login(self):
        self.clear()
        heading=Label(self.root,text='NLPAPP',bg='silver',fg='black')
        heading.pack(pady=(30,30))
        heading.configure(font=('Arial',24, 'bold'))

        label1=Label(self.root,text='Enter Email' ,bg='silver')
        label1.pack(pady=(10,10))

        self.email_input=Entry(self.root,width='40')
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root, text='Enter Password', bg='silver')
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root, width='40', show='*')
        self.password_input.pack(pady=(5,10),ipady=4)

        login_btn=Button(self.root,text='Login',width=20,height=2,command=self.perform_login)
        login_btn.pack(pady=(20,10))

        label3 = Label(self.root, text='Not a member?', bg='silver')
        label3.pack(pady=(10, 10))

        register_btn = Button(self.root, text='Register' ,command=self.register)
        register_btn.pack(pady=(20, 10))

    def register(self):
        self.clear()

        heading = Label(self.root, text='NLPAPP', bg='silver', fg='black')
        heading.pack(pady=(30, 30))
        heading.configure(font=('Arial', 24, 'bold'))

        label0 = Label(self.root, text='Enter Name', bg='silver')
        label0.pack(pady=(5, 5))

        self.name_input = Entry(self.root, width='40')
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text='Enter Email', bg='silver')
        label1.pack(pady=(5, 5))

        self.email_input = Entry(self.root, width='40')
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='Enter Password', bg='silver')
        label2.pack(pady=(5, 5))

        self.password_input = Entry(self.root, width='40', show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_btn = Button(self.root, text='Register', width=20, height=2,command=self.registration_db)
        login_btn.pack(pady=(20, 10))

        label3 = Label(self.root, text='Already a member?', bg='silver')
        label3.pack(pady=(10, 10))

        register_btn = Button(self.root, text='Login Now', command=self.login)
        register_btn.pack(pady=(20, 10))

    def registration_db(self):
        name=self.name_input.get()
        email = self.email_input.get()
        password= self.password_input.get()

        response=self.dbo.add_data(name,email,password)

        if response==1:
           messagebox.showinfo('Success', 'Successfully Registered','You can login now')
        else:
            messagebox.showerror('Error', 'Error Occured')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response=self.dbo.search(email,password)

        if response==1:
            messagebox.showinfo("Success", "Successfully Logged In")
            self.option_menu()
        else:
            messagebox.showerror('Error', 'Error Occured')

    def option_menu(self):
        self.clear()

        heading = Label(self.root, text='NLPAPP', bg='silver', fg='black')
        heading.pack(pady=(30, 30))
        heading.configure(font=('Arial', 24, 'bold'))

        sentiment_btn = Button(self.root, text='Sentiment Analysis',width='30', height='4',
        command=self.sentiment_analysis)
        sentiment_btn.pack(pady=(20, 10))

        ner_btn = Button(self.root, text='NER Analysis', width='30', height='4',
        command = self.ner_analysis)
        ner_btn.pack(pady=(20, 10))

        emotion_btn = Button(self.root, text='Emotion Analysis', width='30', height='4',
        command = self.emotion_analysis)
        emotion_btn.pack(pady=(20, 10))

        logout_btn = Button(self.root, text='Logout', command=self.login)
        logout_btn.pack(pady=(20, 10))

    def sentiment_analysis(self):
        self.clear()

        heading = Label(self.root, text='NLPAPP', bg='silver', fg='black')
        heading.pack(pady=(30, 30))
        heading.configure(font=('Arial', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='silver', fg='black')
        heading2.pack(pady=(30, 30))
        heading2.configure(font=('Arial', 20))

        label1 = Label(self.root, text='Enter the Text', bg='silver')
        label1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width='40')
        self.sentiment_input.pack(pady=(5, 10), ipady=4)

        analyze_btn = Button(self.root, text='Analyze Sentiment', width=20, height=2, command=self.do_sentiment)
        analyze_btn.pack(pady=(20, 10))

        self.sentiment_output = Label(self.root, text='', bg='silver')
        self.sentiment_output.pack(pady=(10, 10))

        self.sentiment_output.configure(font=('Arial', 16))


        go_back_btn = Button(self.root, text='Go To Menu', width=20, height=2, command=self.option_menu)
        go_back_btn.pack(pady=(20, 10))

    def do_sentiment(self):
        text = self.sentiment_input.get()

        if not text.strip():
            messagebox.showerror("Error", "Please enter some text")
            return

        result = self.apio.sentiment_result(text)

        label = result[0]["label"]
        score = result[0]["score"]

        self.sentiment_output.config(
            text=f"Sentiment: {label}\nConfidence: {round(score, 2)}"
        )


    def ner_analysis(self):
            self.clear()

            heading = Label(self.root, text='NLPAPP', bg='silver', fg='black')
            heading.pack(pady=(30, 30))
            heading.configure(font=('Arial', 24, 'bold'))

            heading2 = Label(self.root, text='NER Analysis', bg='silver', fg='black')
            heading2.pack(pady=(20, 20))
            heading2.configure(font=('Arial', 20))

            label1 = Label(self.root, text='Enter the Text', bg='silver')
            label1.pack(pady=(10, 10))

            self.ner_input = Entry(self.root, width='40')
            self.ner_input.pack(pady=(5, 10), ipady=4)

            analyze_btn = Button(self.root, text='Analyze NER', width=20, height=2, command=self.do_ner)
            analyze_btn.pack(pady=(20, 10))

            self.ner_output = Label(self.root, text='', bg='silver', justify=LEFT)
            self.ner_output.pack(pady=(10, 10))
            self.ner_output.configure(font=('Arial', 14))

            go_back_btn = Button(self.root, text='Go To Menu', width=20, height=2, command=self.option_menu)
            go_back_btn.pack(pady=(20, 10))

    def do_ner(self):
        text = self.ner_input.get()
        if not text.strip():
            messagebox.showerror("Error", "Please enter some text")
            return

        entities = self.apio.ner_result(text)

        if not entities:
            self.ner_output.config(text="No entities found.")
            return

        # Format output nicely
        formatted = "\n".join([f"{ent[0]} → {ent[1]}" for ent in entities])
        self.ner_output.config(text=formatted)

    def emotion_analysis(self):
        self.clear()

        heading = Label(self.root, text='NLPAPP', bg='silver', fg='black')
        heading.pack(pady=(30, 30))
        heading.configure(font=('Arial', 24, 'bold'))

        heading2 = Label(self.root, text='Emotion Analysis', bg='silver', fg='black')
        heading2.pack(pady=(20, 20))
        heading2.configure(font=('Arial', 20))

        label1 = Label(self.root, text='Enter the Text', bg='silver')
        label1.pack(pady=(10, 10))

        self.emotion_input = Entry(self.root, width='40')
        self.emotion_input.pack(pady=(5, 10), ipady=4)

        analyze_btn = Button(self.root, text='Analyze Emotion', width=20, height=2, command=self.do_emotion)
        analyze_btn.pack(pady=(20, 10))

        self.emotion_output = Label(self.root, text='', bg='silver')
        self.emotion_output.pack(pady=(10, 10))
        self.emotion_output.configure(font=('Arial', 14))

        go_back_btn = Button(self.root, text='Go To Menu', width=20, height=2, command=self.option_menu)
        go_back_btn.pack(pady=(20, 10))

    def do_emotion(self):
        text = self.emotion_input.get()
        if not text.strip():
            messagebox.showerror("Error", "Please enter some text")
            return

        result = self.apio.emotion_result(text)

        # Check the type of result
        if isinstance(result, list) and isinstance(result[0], list):
            # Some models return [[{'label':..., 'score':...}, ...]]
            items = result[0]
        elif isinstance(result, list) and isinstance(result[0], dict):
            # Some models return [{'label':..., 'score':...}, ...]
            items = result
        else:
            messagebox.showerror("Error", f"Unexpected result format: {result}")
            return

        # Format output
        formatted = "\n".join([f"{item['label']}: {round(item['score'], 2)}" for item in items])
        self.emotion_output.config(text=formatted)

    def clear(self):
        for i in self.root.slaves():
             i.destroy()


nlp =NlpApp()