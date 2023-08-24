import smtplib
import tkinter as tk
from tkinter import *
from tkinter import messagebox  
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import filedialog


class MailingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mail Sending Client.")

        #senders information 
        #email info
        self.sender_mail_label = Label(self.root, text="Sender's Email: ").grid(row=0, column=0, padx=10,pady=10)
        self.sender_mail_entry = Entry(self.root, width=50)
        self.sender_mail_entry.grid(row=0, column=1, columnspan=3, padx=10,pady=10)
        
        #password info
        self.sender_password_label = Label(self.root, text="Sender's Password: ").grid(row=0, column=4, padx=10,pady=10)
        self.sender_password_entry = Entry(self.root, width=50, show="*")
        self.sender_password_entry.grid(row=0, column=5, columnspan=3, padx=10,pady=10)

        #receivers information
        #email info
        self.receiver_mail_label = Label(self.root, text="Receiver's Email: ").grid(row=1, column=0, padx=10, pady=10)
        self.receiver_mail_entry = Entry(self.root, width=50)
        self.receiver_mail_entry.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

        #subject info 
        self.subject_label = Label(self.root, text="Subject: ").grid(row=1, column=4, padx=10, pady=10)
        self.subject_entry = Entry(self.root, width=50)
        self.subject_entry.grid(row=1, column=5, columnspan=3, padx=10, pady=10)

        #body/message info
        self.body_label = Label(self.root, text="Body: ").grid(row=2, column=0, padx=10, pady=10)
        self.body_text = Text(self.root, width=102, height=20)
        self.body_text.grid(row=3, column=0, columnspan=10, padx=10, pady=10)
        
        # Send Email button
        self.send_button = Button(self.root, text="Send Email", command=self.send_email)
        self.send_button.grid(row=4, column=0, padx=10, pady=10)
        
    def send_email(self):
        # get all the information available and store them inside variables
        sender_email = self.sender_mail_entry.get()
        sender_password = self.sender_password_entry.get()
        recipient_email = self.receiver_mail_entry.get()
        subject = self.subject_entry.get()
        body = self.body_text.get("1.0", "end-1c")

        #create email msg headers
        #MIME = Multipurpose internet mailing extension 
        msg = MIMEMultipart()
        #setting the 'from' header, who the email is sent from
        msg['From'] = sender_email
        #setting the 'to' header, who the email is concerned to
        msg['To'] = recipient_email
        #setting the 'subject' header, msg or body portion of the mail.
        msg['Subject'] = subject

        #setting up of a server, creates an instance of smtp() class for connecting gmail's smtp server on specified port(587)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        #starts a secure smtp server connection using tls(transport layer security) 
        server.starttls()
        #logs into smtp server using the credentials. Important step for authentication 
        server.login(sender_email, sender_password)
        #sends the email, specifies the sender's mail, recipient's mail, and email message as string  
        server.sendmail(sender_email, recipient_email, msg.as_string())
        #closing the connection to the smtp server
        server.quit()
        #success message 
        messagebox.showinfo("Success", "Email sent successfully!")

root = tk.Tk()
mailing_app = MailingApp(root)
root.mainloop()
