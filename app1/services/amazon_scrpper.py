import requests

headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
    "action": "sign-in",
    "email": "6280869135",
    "password": "Mohan@123"
}

def amazon(url):
    r = requests.get(url, headers=headers)
    html_content = r.content



