import re


text = 'My number is 415-223-4313\n 342-412-4123'
phone_regex = re.compile(r'(\d{3})-(\d{3}-\d{4})', re.I | re.VERBOSE | re.DOTALL)
phone = phone_regex.findall(text)
print(phone[1])
