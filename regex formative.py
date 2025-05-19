import re
text = """
Contact us at marketing@thepinnaclekigali.com or visit https://www.thepinnaclekigali.com. You can also call 0790223201 for bookings before 11:00 AM or after 14:00.
"""
# Find all email addresses
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, text)
print("The email address:", emails)
# Find all URLs
url_pattern = r'(https?://[^\s]+|www\.[^\s]+)'
urls = re.findall(url_pattern, text)
print("URLs in text:", urls)
# Find all phone numbers
phone_pattern = r'\b\d{10}\b|\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'
phones = re.findall(phone_pattern, text)
print("Phone numbers to reach out to:", phones)
# Find all times
time_24hr_pattern = r'\b([01]?[0-9]|2[0-3]):[0-5][0-9]\b'
time_12hr_pattern = r'\b(1[0-2]|0?[1-9]):[0-5][0-9]\s?(AM|PM|am|pm)\b'
time_pattern = f'({time_24hr_pattern}|{time_12hr_pattern})'
times = re.findall(time_pattern, text)
print("Working hours:", [t[0] for t in times])
