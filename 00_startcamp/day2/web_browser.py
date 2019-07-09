import webbrowser

urls = [
    'https://github.com',
    'https://google.com',
    'https://naver.com',
    'https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4',
    'https://edu.ssafy.com'
    ]

# n = 0
# while urls[n] != None:
#     webbrowser.open(urls[n])
#     n += 1

for url in urls:
    webbrowser.open(url)
