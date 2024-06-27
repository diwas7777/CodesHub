import tkinter as tk
from tkinter import messagebox, filedialog
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def browse_file():
    file_path = filedialog.askopenfilename()
    attachment_entry.delete(0, tk.END)
    attachment_entry.insert(tk.END, file_path)
    
def clear_fields():
    recipient_entry.delete(0, tk.END)
    subject_entry.delete(0, tk.END)
    message_text.delete("1.0", tk.END)
    attachment_entry.delete(0, tk.END)
    
def send_mail():
    recipient = recipient_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END)

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'ENTER_YOUR_EMAIL_ADDRESS'
    smtp_password = 'ENTER_YOUR_EMAIL_APP_PASSWORD'
    
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    
    attachment_path = attachment_entry.get()
    if attachment_path:
        attachment = open(attachment_path, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {attachment_path}")
        msg.attach(part)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, recipient, msg.as_string())
        server.quit()
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        if recipient=="":
            messagebox.showerror("Error","Recepient address not found")
            return 0
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

window = tk.Tk()
window.title("Mail Application")
window.configure(bg="#f5f5f5")
window.geometry("450x350")
window.resizable(True,True)

title_label = tk.Label(window, text="Mail Application", font=("TimesNewRoman", 16, "bold"), bg="#f5f5f5")
title_label.pack(pady=10)

recipient_frame = tk.Frame(window, bg="#f5f5f5")
recipient_frame.pack(pady=5)
recipient_label = tk.Label(recipient_frame, text="Recipient:", bg="#f5f5f5", font=("TimesNewRoman", 12))
recipient_label.pack(side=tk.LEFT)
recipient_entry = tk.Entry(recipient_frame, font=("TimesNewRoman", 12), width=30)
recipient_entry.pack(side=tk.LEFT)

subject_frame = tk.Frame(window, bg="#f5f5f5")
subject_frame.pack(pady=5)
subject_label = tk.Label(subject_frame, text="Subject:", bg="#f5f5f5", font=("TimesNewRoman", 12))
subject_label.pack(side=tk.LEFT)
subject_entry = tk.Entry(subject_frame, font=("TimesNewRoman", 12), width=30)
subject_entry.pack(side=tk.LEFT)

message_frame = tk.Frame(window, bg="#f5f5f5")
message_frame.pack(pady=5)
message_label = tk.Label(message_frame, text="Message:", bg="#f5f5f5", font=("TimesNewRoman", 12))
message_label.pack(side=tk.LEFT)
message_text = tk.Text(message_frame, font=("Algeria", 12), width=30, height=5)
message_text.pack(side=tk.LEFT)

attachment_frame = tk.Frame(window, bg="#f5f5f5")
attachment_frame.pack(pady=5)
attachment_label = tk.Label(attachment_frame, text="Attachment:", bg="#f5f5f5", font=("TimesNewRoman", 12))
attachment_label.pack(side=tk.LEFT)
attachment_entry = tk.Entry(attachment_frame, font=("TimesNewRoman", 12), width=25)
attachment_entry.pack(side=tk.LEFT)
browse_button = tk.Button(attachment_frame, text="Browse", font=("TimesNewRoman", 10), command=browse_file)
browse_button.pack(side=tk.LEFT)

send_button = tk.Button(window, text="Send", font=("TimesNewRoman", 12, "bold"),bg="#fff",fg="#000", command=send_mail)
send_button.pack(pady=10)

clear_button=tk.Button(window,text="Clear",font=("TimesNewRoman",12,"bold"),bg="#f5f5f5",command=clear_fields)
clear_button.pack(pady=10)

window.mainloop()
