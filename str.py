#all about strings
emails = '''
Hello John,

We are glad to have you i our team as we get ready for the upcoming project
Regards,
Eugene Kabeyi
C.E.O White Deco LTD.
'''
print(emails)

book = "Think and Grow Rich"
print(book[-9:15])

first= "John"
last= "Doe"
msg = f'{first} {last} is a good person\n'
print(msg)

print(len(msg))
print(msg.upper())
print(msg.find("o"))
print(msg.replace('good person','fantastic individual\n'))
print('good' in msg)


