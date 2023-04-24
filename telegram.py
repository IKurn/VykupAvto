import requests
import cgi

form = cgi.FieldStorage()
name = form.getvalue('name')
phone = form.getvalue('phone')
car = form.getvalue('car')

def send_msg(name, phone, car):
   token = "6034701467:AAHNu53DefssEDJAz-BFgIN6bOcJFESPysc"
   #chat_id = "-1001783612572"
   chat_id = "-909118769"
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + '8======D' 
   results = requests.get(url_req)
   print(results.json())

send_msg(name, phone, car)
