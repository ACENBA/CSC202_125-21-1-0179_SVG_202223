import smtplib
my_email = "adewalep096@gmail.com"
password = "emperor11@"

try:
    connection = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is the port number for TLS
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="adewalep097@gmail.com", msg="Subject:This is the practical sample")
    connection.quit()  # Use quit() instead of close()
    print("Email sent successfully!")
except smtplib.SMTPAuthenticationError:
    print("Error: Authentication failed. Check your email and password.")
except smtplib.SMTPException as e:
    print("Error sending email:", e)
except Exception as e:
    print("An unexpected error occurred:", e)

