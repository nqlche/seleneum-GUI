from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import csv


def dowloand_data(url, file_name):
    # print('Processing...')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    with webdriver.Chrome(options=options) as browser:
        browser.get(url)
        browser.maximize_window()
        time.sleep(1)
        b1 = browser.find_element(By.ID, 'peer_type_chat')
        ActionChains(browser).move_to_element(b1).click().perform()
        time.sleep(2)
        while True:
            try:
                ActionChains(browser).move_to_element(browser.find_element(By.CSS_SELECTOR,
                                                                           "button[class='btn btn-light border lm-button py-1 min-width-220px']")).click().perform()
            except:
                # print('Прогрузка сайта завершена')
                html_ = browser.page_source
                break
            finally:
                time.sleep(1)
        with open(f'{file_name}.csv', 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['линк', 'Ссылка', 'Название', 'Кол-во участников', 'Последние сообщение'])
        collect_data(file_name, html_=browser.page_source)


def collect_data(n, html_):
    soup = BeautifulSoup(html_, 'lxml')
    cards = soup.find_all('div', class_='col-12 col-sm-6 col-md-4')
    for i in cards:
        link = i.find('a', class_='text-body')['href']
        link_ref = f"https://t.me{link.split('tgstat.ru/chat')[-1].replace('@', '')}"
        link_1_stolb = link.split('tgstat.ru/chat')[-1].replace('@', '').replace('/', '')
        title = i.find('div', class_='font-16 text-dark text-truncate').text.strip()
        members = i.find('div', 'font-12 text-truncate').find('b').text.strip()
        last_msg = f"   {i.find('div', class_='text-center text-muted font-12').text.strip()}"

        with open(f'{n}.csv', 'a', encoding='utf-8-sig', newline='') as file_a:
            flatten = link_1_stolb, link_ref, title, members, last_msg
            writer = csv.writer(file_a, delimiter=';')
            writer.writerow(flatten)
    # print('Файл создан')

# def main():
#     dowloand_data(url=input('Введите ссылку: '), n=input('Введите имя файла загрузки'))
#
#
# if __name__ == '__main__':
#     main()
