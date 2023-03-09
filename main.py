import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()
email_list = {
    "sujahath" : "sujahathmhmd@gmail.com",
    "altaccs" : "myaltaccs852@gmail.com",
    "rahman" : "mhmdsjthrhmn@gmail.com"
}
def talk(text):
    engine.say(text)
    engine.runAndWait()
def getInfo():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        print("Error")


def sendMail(receiver, subject, message):
    # smtplib - Simple Mail Transfer Protocol
    server = smtplib.SMTP("smtp.gmail.com", 587)  # an interconnecting member
    server.starttls()  # telling the server, that we are sending this mail in a secure way
    # Senders Details
    s_email = "sujahathmsm98@gmail.com"
    s_password = "kgfwqmpohljqizwe"
    # login
    server.login(s_email, s_password)

    # send mail
    email = EmailMessage()
    email["From"] = s_email
    email["To"] = receiver
    email["Subject"] = subject
    email.set_content(message)
    server.sendmail(email)
    print("---Your Mail has been sent succesfully!, Thank you for using our service")

def get_mail_info():
    talk("To whom you want to send email? ")
    talk("Dont worry, I will take care about it")
    name = getInfo()
    receiver = email_list[name]
    print(receiver)
    talk("What is the subject")
    subject = getInfo()
    talk("Tell me the content of your email")
    message = getInfo()
    sendMail(receiver, subject, message)



get_mail_info()