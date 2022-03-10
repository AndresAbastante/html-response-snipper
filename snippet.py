from asyncio.format_helpers import extract_stack
from pydoc import resolve
import re
import requests
import os
import sys

url = 'insert_your_target_url'

#turning the 'request.txt' file (in the script folder) into the string variable 'text_file'
with open(os.path.join(sys.path[0], "request.txt"),"r") as text_file:
    request=text_file.read()
    text_file.close()

print("##############REQUEST############## \n###################################")
print(request)

#sending the method over the 'response' variable
response = requests.post(url, data = request)

print("##############RESPONSE############## \n###################################")
response_text=response.text
print(response_text)

#extracting relevant data from the response string
print("#############EXTRACTING############# \n####################################")

#print() would extract everything 
#extract=response_text.partition('text_parameter')[2] snippets everything after the text_parameter 
#extract=re.split("text_parameter+", response_text) snippets every instance of text_parameter found 

#find $ print the first character's position
start = response_text.find("first_string_to_find") + len("first_string_to_find") 
print(start)

#find & print the last character's position
end = response_text.find("last_string_to_find")
print(end)

#cut the string to desirable size
extract = response_text[start:end]
print(extract)