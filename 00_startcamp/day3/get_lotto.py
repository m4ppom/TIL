import requests
import json
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'
response = requests.get(url).text
# text = bs4.BeautifulSoup(response, 'html.parser')
# no = text.select_one()
data = json.loads(response)

real_numbers = []
# for i in range(6):
#     real_numbers[i] = data[f'drwtNo{i+1}']
# print(real_numbers)

for key, value in data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)
print(real_numbers)
# {
#     "totSellamnt":81961886000,
#     "returnValue":"success",
#     "drwNoDate":"2019-07-06",
#     "firstWinamnt":2240409000,
#     "drwtNo6":39,
#     "drwtNo4":34,
#     "firstPrzwnerCo":9,
#     "drwtNo5":37,
#     "bnusNo":12,
#     "firstAccumamnt":20163681000,
#     "drwNo":866,
#     "drwtNo2":15,
#     "drwtNo3":29,
#     "drwtNo1":9
# }
