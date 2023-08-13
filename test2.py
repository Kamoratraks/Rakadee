from selenium import webdriver
from selenium.webdriver.common.by import By
from fastapi import FastAPI
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

get1 = "computer"
driver = webdriver.Chrome()
driver.get('https://www.amazon.com/?&tag=googleglobalp-20&ref=pd_sl_7nnedyywlk_e&adgrpid=82342659060&hvpone=&hvptwo=&hvadid=393493755082&hvpos=&hvnetw=g&hvrand=10520968507142495629&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9073373&hvtargid=kwd-10573980&hydadcr=2246_11061421')
time.sleep(0.5)


s =driver.find_element(By.XPATH,' /html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
s.send_keys(get1)
time.sleep(0.5)

s_click = driver.find_element(By.XPATH, value=' /html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
s_click.click()
time.sleep(0.5)
driver.execute_script("document.body.style.zoom='50%'")
time.sleep(2)

NAME_A1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2').text
Price_A1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a/span').text
image_elements_A1 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img')
image_links_A1 = [img.get_attribute('src') for img in image_elements_A1]
product_links_A1 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/span/a')
product_urls_A1 = [img.get_attribute('href') for img in product_links_A1]


print(NAME_A1)
print(Price_A1)
print(image_links_A1)
print(product_urls_A1)
print("")


NAME_A2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2').text
Price_A2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a/span').text
image_elements_A2 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img')
image_links_A2 = [img.get_attribute('src') for img in image_elements_A2]
product_links_A2 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/span/a')
product_urls_A2 = [img.get_attribute('href') for img in product_links_A2]

print(NAME_A2)
print(Price_A2)
print(image_links_A2)
print(product_urls_A2)
print("")

                                        
NAME_A3 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[2]/div/div/div[1]/h2').text
Price_A3 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/a/span/span[2]').text
image_elements_A3 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img')
image_links_A3 = [img.get_attribute('src') for img in image_elements_A3]
product_links_A3 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[1]/div/div[2]/div/span/a')
product_urls_A3 = [img.get_attribute('href') for img in product_links_A3]

print(NAME_A3)
print(Price_A3)
print(image_links_A3)
print(product_urls_A3)
print("")


NAME_A4 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div/div[2]/div/div/div[1]/h2').text
Price_A4 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/a/span/span[2]').text
image_elements_A4 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div')
image_links_A4 = [img.get_attribute('src') for img in image_elements_A4]
product_links_A4 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div/div[1]/div/div[2]/div/span/a')
product_urls_A4 = [img.get_attribute('href') for img in product_links_A4]

print(NAME_A4)
print(Price_A4)
print(image_links_A4)
print(product_urls_A4)
print("")

NAME_A5 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div/div[2]/div/div/div[1]/h2').text
Price_A5 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/a/span/span[2]').text
image_elements_A5 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img')
image_links_A5 = [img.get_attribute('src') for img in image_elements_A5]
product_links_A5 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div/div[1]/div/div[2]/div/span/a')
product_urls_A5 = [img.get_attribute('href') for img in product_links_A5]

print(NAME_A5)
print(Price_A5)
print(image_links_A5)
print(product_urls_A5)
print("")
print("=================================================================================================================================================")

