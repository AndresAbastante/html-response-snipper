from asyncio.format_helpers import extract_stack
from pydoc import resolve
import re
import requests
import os
import sys

url = 'insert_your_target_url'

#Turning the 'request.txt' file (in the script folder) into the string variable 'text_file'
with open(os.path.join(sys.path[0], "request.txt"),"r") as text_file:
    request=text_file.read()
    text_file.close()

print("##############REQUEST############## \n###################################")
print(request)

#Sending the method over the 'response' variable
response = requests.post(url, data = request)

print("##############RESPONSE############## \n###################################")
response_text=response.text
print(response_text)

#Setting fist and last string targets. They need to be unique, kinda sucks tbh.
first_string="insert the string parameter before your target"
last_string="insert the string parameter after your target"

#Find & print the first character's position.
start = response_text.find("first_string") + len("first_string") 
print(start)

#Find & print the last character's position.
end = response_text.find("last_string")
print(end)

#Extracting relevant data from the response string.
print("#############EXTRACTING############# \n####################################")

#Print() would extract everything.
#Extract=response_text.partition('text_parameter')[2] snippets everything after the text_parameter 
#Extract=re.split("text_parameter+", response_text) snippets every instance of text_parameter found 

#Cut the string to desirable size.
extract = response_text[start:end]
print(extract)
