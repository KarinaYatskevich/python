# import requests
# import fake_useragent
# from bs4 import BeautifulSoup
#
# user = fake_useragent.UserAgent().random
# header = {'user-agent': user}
# # скачает все с сайта
# # link = 'https://browser-info.ru/'
# # responce = requests.get(link).text
# # print(responce.text)
# # print(responce.status_code)
# #запишет весь материал в новый файл
# # with open('files/parser.html', 'w', encoding = "utf-8") as file:
# #     file.write(responce)
#
# link = 'https://browser-info.ru/'
# responce = requests.get(link, headers = header).text
# soup = BeautifulSoup(responce, "lxml")
# block = soup.find('div', id = 'tool_padding')
#
# # check js
# check_js = block.find('div', id = "javascript_check")
# status_js = check_js.find_all('span')[1].text
# result_js = f'Javascript: {status_js}'
#
# # check flash
# check_flash = block.find('div', id = "flash_version")
# status_flash = check_flash.find_all('span')[1].text
# result_flash = f'flash: {status_flash}'
#
# # check user-agent
# check_user = block.find('div', id = "user_agent").text
#
#
# print(result_js)
# print(result_flash)
# print(check_user)
