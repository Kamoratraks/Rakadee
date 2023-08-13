from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time

text = input("Search Item : ")
driver = webdriver.Chrome()
driver.get('https://www.amazon.com/?&tag=googleglobalp-20&ref=pd_sl_7nnedyywlk_e&adgrpid=82342659060&hvpone=&hvptwo=&hvadid=393493755082&hvpos=&hvnetw=g&hvrand=10520968507142495629&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9073373&hvtargid=kwd-10573980&hydadcr=2246_11061421')
time.sleep(0.5)


def searchitem ():
    s =driver.find_element(By.XPATH,' /html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
    s.send_keys(text)
    time.sleep(0.5)

    s_click = driver.find_element(By.XPATH, value=' /html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
    s_click.click()
    time.sleep(2)

    NAME1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span').text
    Price1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/a/span/span[2]').text
    image_elements1 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img')
    image_links1 = [img.get_attribute('src') for img in image_elements1]
    product_links1 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/span/a')
    product_urls1 = [img.get_attribute('href') for img in product_links1]
    star = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/span[1]/span/a/i[1]/span')

    print(NAME1)
    print(Price1)
    print(image_links1)
    print(product_urls1)
    print(star)
    print("")
    '''
    NAME2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span').text
    Price2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a/span/span[2]').text
    image_elements2 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img')
    image_links2 = [img.get_attribute('src') for img in image_elements2]
    product_links2 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/span/a')
    product_urls2 = [img.get_attribute('href') for img in product_links2]

    print(NAME2)
    print(Price2)
    print(image_links2)
    print(product_urls2)
    print("")

    NAME3 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span').text
    Price3 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a/span/span[2]').text
    image_elements3 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img')
    image_links3 = [img.get_attribute('src') for img in image_elements3]
    product_links3 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div/div[1]/div/div[2]/div/span/a')
    product_urls3 = [img.get_attribute('href') for img in product_links3]

    print(NAME3)
    print(Price3)
    print(image_links3)
    print(product_urls3)
    print("")
   

    NAME4 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span').text
    Price4 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a/span/span[2]').text
    image_elements4 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img')
    image_links4 = [img.get_attribute('src') for img in image_elements4]
    product_links4 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[1]/div/div[2]/div/span/a')
    product_urls4 = [img.get_attribute('href') for img in product_links4]
    
    print(NAME4)
    print(Price4)
    print(image_links4)
    print(product_urls4)
    print("")

    NAME5 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span').text
    Price5 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a/span/span[2]').text
    image_elements5 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img')
    image_links5 = [img.get_attribute('src') for img in image_elements5]
    product_links5 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div/div[1]/div/div[2]/div/span/a')
    product_urls5 = [img.get_attribute('href') for img in product_links5]

    print(NAME5)
    print(Price5)
    print(image_links5)
    print(product_urls5)
    print("")
    '''
searchitem ()