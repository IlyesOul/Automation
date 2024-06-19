# Import smtplib for the actual sending function
import smtplib
import csv
import math_programs

# Import the email modules we'll need
from email.mime.text import MIMEText

# Storing email
def store_email():
    subject = "Eager High School Junior Looking for Internship Experience"
    name = input("Contact first name? ")
    company = input("Company name? ")
    category = int(input("Quantitative firm (0) or tech company (1)? "))
    email = input("Contact email?")

    if category == 0:
        content=f"Hello {name}, \n\nI hope this email finds you well. My name is Ilyes Ouldsaada and I’m a high school Junior who’s deeply passionate about machine learning and financial markets. Having researched {company}'s market-leading and innovative work in automated quantitative trading, I’d appreciate the opportunity to learn more over a call or meeting.\nMy studies and experiences include:\n\n - Dual-enrollment college classes in Data Structures and Algorithms \n - Self-studying machine learning independently over the school year\n - Developing a program that solves stock hold duration via machine learning, statistical regression, and technical analysis\n - Competing in MIT's Blueprint competition and winning Hackclub's 24 programming competition, AngelHacks\n\nI am eager to jumpstart my experiences in business and would sincerely appreciate the opportunity to intern or job-shadow at {company}.\n\nPlease refer to this link for my portfolio: https://ilyesoul.github.io/Portfolio_Web/\nMy resume is attached to this email and your time is much appreciated.\n\nBest,\nIlyes Ouldsaada"
        print(content)

    # Write info to file
    with open('emails.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Company Name", "Contact", "Email", "Content"])
        writer.writerow([company, name, email, content])


# Send emails in CSV file
def send_emails():

