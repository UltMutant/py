import mechanicalsoup
browser = mechanicalsoup.Browser()
url = "https://www.example.com"
response = browser.get(url)
soup = response.soup
links = soup.find_all('a')
for link in links:
    print(link.get('href'))