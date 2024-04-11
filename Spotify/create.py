import undetected_chromedriver
from undetected_chromedriver import Chrome, ChromeOptions
from discord import SyncWebhook
import random
import string
from time import sleep
from random import choices
import json
from colorama import Fore, Back
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
#self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[1]/div/input').send_keys(self.password)
class marielsahtepydev():
    def main():
        try:
            with open('./proxy/proxys.data','r') as f:
                    proxys = f.readlines()
            proxyler = random.choice(proxys).strip()  
            webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/1226937791464734760/SdvN2mrPeXDd7aEi_hdoh6TxFM__uPD3te8V8lsUs9EBom-pTTuUdJA1WYv3TnFsTjUE")
            options = ChromeOptions()
            options.add_extension('solver.crx') 
            #options.add_argument(f'--proxy-server={proxyler}')
            #options.add_argument("--headless")
            driver = Chrome(options=options)
            with open('config.json', 'r') as f:
                    config_data = json.load(f)
            with open("names.txt", "r", encoding="utf-8") as file:
                            names = file.readlines()
            secilen_isim = random.choice(names).strip()  
            karakter_ekleme_miktari = 16 - len(secilen_isim)
            random_sayilar = ''.join(random.choice(string.digits) for _ in range(karakter_ekleme_miktari))
            username = secilen_isim + random_sayilar
            DateMonth = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                                "11", "12"])
            selected_month_value = DateMonth
            DateDay = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                                    "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                                    "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"])
            DateYear = [str(year) for year in range(1990, 2006)]
            password_sayıları =  ''.join(choices('abcdefghijklmnopqrstuvwxyz12345687989', k=6))
            password = password_sayıları + "_Hotline_BY_WUPLISH"
            email =  ''.join(choices('abcdefghijklmnopqrstuvwxyz12345687989', k=12)) + "@gmail.com"
            driver.get("https://www.spotify.com/tr-tr/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2Fintl-tr")
            driver.find_element(By.CSS_SELECTOR, '[id="username"]').send_keys(email)
            sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/main/main/section/div/form/button/span[1]').click()
            sleep(2)
            driver.find_element(By.CSS_SELECTOR, '[id="new-password"]').send_keys(password)
            sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/main/main/section/div/form/div[2]/button/span[1]').click()
            sleep(2)
            driver.find_element(By.CSS_SELECTOR, '[id="displayName"]').send_keys(username)
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[id="day"]').send_keys(DateDay)
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[id="year"]').send_keys(DateYear)
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '[id="onetrust-accept-btn-handler"]').click()
            select_box = Select(driver.find_element(By.ID, 'month'))
            select_box.select_by_value(selected_month_value)
            sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/main/main/section/div/form/div[1]/div[2]/div/section/div[3]/fieldset/div/div/div[1]/label/span[1]').click()
            sleep(2)
            driver.find_element(By.XPATH, '/html/body/div[1]/main/main/section/div/form/div[2]/button/span[1]').click()
            sleep(2)
            driver.find_element(By.XPATH, '/html/body/div[1]/main/main/section/div/form/div[1]/div[2]/div/section/div[4]/div[1]/div/div/label/span[1]').click()
            driver.find_element(By.XPATH, '/html/body/div[1]/main/main/section/div/form/div[1]/div[2]/div/section/div[4]/div[2]/div/label/span[1]').click()
            sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/main/main/section/div/form/div[2]/button/span[1]').click()
            sleep(9)
            current_url = driver.current_url
            if current_url == "https://open.spotify.com/intl-tr":
                with open('./acc/acc.data','a') as handler:
                    handler.write(f'{email}:{password}\n')
                print(Fore.GREEN,Back.GREEN,f"Account Created :      {email}    |    {username}     |    {password}",Fore.RESET,Back.RESET)
                webhook.send(f"Account Created :      {email}    |    {username}     |    {password}")
            else:
                print(Fore.RED,Back.RED,"Account Not Created :(  ",Fore.RESET,Back.RESET)
                webhook.send("Account Not Created :(")
                import sys
                sys.exit()
                
            sleep(3)
            spotify_url = config_data.get('username_url')
            print(Fore.GREEN,Back.GREEN,f"Following {spotify_url}",Fore.RESET,Back.RESET)
            driver.get(spotify_url)
            sleep(5)
            driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/main/section/div/div[3]/div[2]/div/div/button[1]').click()
            sleep(1)
            print(Fore.GREEN,Back.GREEN,"Followed Easy! :)",Fore.RESET,Back.RESET) 
            driver.close()
        except:
            print(Fore.RED,Back.RED,"ERROR!",Fore.RESET,Back.RESET)
            driver.close()

bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
bot = marielsahtepydev
bot.main()
