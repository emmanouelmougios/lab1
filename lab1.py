import requests
import datetime

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break
            
def headers(response):                         # print headers
    
    # Print the server software
    if 'Server' in response.headers:
        print("\nServer software:", response.headers['Server'])
    else:
        print("\nServer software information not available.")
        
    print("\nHeaders of the HTTP response: \n")
    i = 0
    for key, value in response.headers.items():
        header_dict = {key: value}
        print(header_dict)
        i += 1
        if i % 10 == 0:
            reply = input('\nShow more headers (y/n)? ')
            if reply == 'n':
                break
            
         
def cookies(response):                       # print cookies
    print("\nCookies: \n")
    i = 0
    for cookie in response.cookies:
        cookie_dict = {cookie.name: cookie.value}
        print(cookie_dict)
        if cookie.expires:
            expires_date = datetime.datetime.fromtimestamp(cookie.expires)
            print("Expires:", expires_date)
        i += 1
        if i % 10 == 0:
            reply = input('\nShow more cookies (y/n)? ')
            if reply == 'n':
                break
            
                    

url = input("Please enter the URL: ")  

with requests.get(url) as response:    # http request
    html = response.text
    headers(response)
    cookies(response)
    #more(html)