# Import necessary libraries
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

# Initialize SpeechRecognition and pyttsx3 instances
listener = sr.Recognizer()
engine = pyttsx3.init()

# Define a dictionary of email addresses for different recipients
email_list = {
    "sujahath" : "sujahathmhmd@gmail.com",
    "altaccs" : "myaltaccs852@gmail.com",
    "rahman" : "mhmdsjthrhmn@gmail.com"
}

# Function to convert text to speech
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Function to get information from the user via microphone input
def getInfo():
    try:
        with sr.Microphone() as source:
            # Let the user know that the function is listening
            print("Listening....")
            # Listen to the user's voice and store it as audio data
            voice = listener.listen(source)
            # Convert the audio data into text using Google's Speech Recognition API
            info = listener.recognize_google(voice)
            # Print the recognized text to the console
            print(info)
            # Return the recognized text in lowercase
            return info.lower()
    # If an error occurs during the execution of the function, catch it and print an error message
    except:
        print("Error")

# Function to send an email
def sendMail(receiver, subject, message):
    # Initialize an SMTP server for Gmail
    server = smtplib.SMTP("smtp.gmail.com", 587)
    # Start a secure connection with the SMTP server
    server.starttls()
    # Enter the sender's details
    s_email = "sujahathmsm98@gmail.com"
    s_password = "kgfwqmpohljqizwe"
    # Login to the sender's email account
    server.login(s_email, s_password)

    # Construct the email message
    email = EmailMessage()
    email["From"] = s_email
    email["To"] = receiver
    email["Subject"] = subject
    email.set_content(message)
    # Send the email
    server.sendmail(email)
    # Let the user know that the email has been sent successfully
    print("---Your Mail has been sent successfully!, Thank you for using our service")

# Function to get email information from the user
def get_mail_info():
    # Ask the user to whom they want to send the email
    talk("To whom you want to send email? ")
    talk("Don't worry, I will take care about it")
    name = getInfo()
    # Look up the recipient's email address based on their name
    receiver = email_list[name]
    print(receiver)
    # Ask the user for the email subject
    talk("What is the subject")
    subject = getInfo()
    # Ask the user for the email content
    talk("Tell me the content of your email")
    message = getInfo()
    # Send the email using the information provided by the user
    sendMail(receiver, subject, message)
    talk("Hey ur mail is sent")
    talk("Do you want to send more email? ")
    send_more = getInfo()
    if "yes" in send_more:
        get_mail_info()


# Call the function to get email information from the user and send the email
get_mail_info()
