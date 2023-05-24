import requests
def url_ok(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError as e:
        return e
url = "https://www.google.com"
if url_ok(url):
    print("Website is live")
else:
    print("Website not live")