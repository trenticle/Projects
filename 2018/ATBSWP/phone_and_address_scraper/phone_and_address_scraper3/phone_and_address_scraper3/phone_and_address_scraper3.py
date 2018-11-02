# 1 Create a regex for phone numbers
# 2 Create a regex for email addresses
# 3 Get the text off the clipboard
# 4 Extract the email/phone from this text
# ToDo: Copy the extracted email/phone to the clipboard

import pyperclip
import re

# 1
phoneRegex = re.compile(r'''
# phone number regex's based on the following:
# 000-00-0000, 000-0000, (000) 000-0000, 000-0000 ext 00000, ext. 00000, x00000

# 1.1 area code (optional)
((\d\d\d)|(\(\d\d\d\)))?

# 1.2 first separator
(\s|-)

# 1.3 first 3 digits
\d\d\d

# 1.4 separator
(\s|-)

# 1.5 last 4 digits
\d\d\d\d

# 1.6.1 optional extension (alpha)
(((ext(\.)?\s)|x)

# 1.6.2 optional extension (num)
    (\d{2,5}))?
''', re.VERBOSE)

# 2
emailRegex = re.compile(r'''
# email regex's based on the following:
# some.+_thing@some.+-thing.com

# 2.1 name part
[a-zA-z0-9.+_]+
# 2.2 "@" symbol
@
# 2.3 domain name part
[a-zA-z0-9.+_]+
''', re.VERBOSE)

# 3 
text = pyperclip.paste()

# 4 
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

print(extractedPhone)
print(extractedEmail)


