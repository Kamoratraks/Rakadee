from selenium import webdriver
from selenium.webdriver.common.by import By
import time

text = input("Search Item : ")
driver = webdriver.Chrome()
driver.get('https://shopee.co.th/search?keyword=rtx%203060')
time.sleep(2)

gg = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[1]/div[1]/div/div[3]/div[1]/button')
gg.click()
time.sleep(2)
'''
close = driver.execute_script('return document.querySelector("shopee-banner-popup-stateful").shadowRoot.querySelector("div.shopee-popup__close-btn")')
close.click()
time.sleep(2)
'''

s =driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/header/div[2]/div/div[1]/div[1]/div/form/input')
s.send_keys(text)
time.sleep(2)

s_input = driver.find_element(by=By.XPATH, value=' /html/body/div[1]/div/header/div[2]/div/div[1]/div[1]/button')
s_input.click()
time.sleep(2)


'''NAME = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/a[1]/div/div[2]').text
print(NAME)'''
