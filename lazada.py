from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import requests
import time





def Searchitem ():
    
    driver = webdriver.Chrome()
    driver.get('https://www.lazada.co.th/?trafficFrom=17449020_308357&laz_trackid=2:mm_150221168_51502798_2010502795:clkgk1m851h66b392v2ul1&mkttid=clkgk1m851h66b392v2ul1')
    
    s =driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/form/div/div[1]/input[1]')
    s.send_keys(text1)
    
    s_click = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/form/div/div[2]/button')
    s_click.click()
    
    driver.execute_script("document.body.style.zoom='10%'")
    
    NAME1 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a').text
    Price1 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/span').text
    image_elements1 = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div[1]/a/div/img')
    image_links1 = [img.get_attribute('src') for img in image_elements1]
    product_links1 = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div[1]/a')
    product_urls1 = [img.get_attribute('href') for img in product_links1]

    print(NAME1)
    print(Price1)
    print(image_links1)
    print(product_urls1)
    print("")

    NAME2 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/a').text
    Price2 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div[3]/span').text
    image_elements2 = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/a/div/img')
    image_links2 = [img.get_attribute('src') for img in image_elements2]
    product_links2 = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div[10]/div[1]/div[1]/div/div/div/div/div[1]/div')
    product_urls2 = [img.get_attribute('href') for img in product_links2]

    print(NAME2)
    print(Price2)
    print(image_links2)
    print(product_urls2)
    print("")

    NAME3 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/a').text
    Price3 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[3]/span').text
    image_elements3 = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/a/div/img')
    image_links3 = [img.get_attribute('src') for img in image_elements3]
    product_links3 = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/a')
    product_urls3 = [img.get_attribute('href') for img in product_links3]

    print(NAME3)
    print(Price3)
    print(image_links3)
    print(product_urls3)
    print("")
   

    NAME4 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[4]/div/div/div[2]/div[2]/a').text
    Price4 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[4]/div/div/div[2]/div[3]/span').text
    image_elements4 = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[4]/div/div/div[1]/div[1]/a/div/img')
    image_links4 = [img.get_attribute('src') for img in image_elements4]
    product_links4 = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[4]/div/div/div[1]/div[1]/a')
    product_urls4 = [img.get_attribute('href') for img in product_links4]
    
    print(NAME4)
    print(Price4)
    print(image_links4)
    print(product_urls4)
    print("")

    NAME5 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[5]/div/div/div[2]/div[2]/a').text
    Price5 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[5]/div/div/div[2]/div[3]/span').text
    image_elements5 = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[5]/div/div/div[1]/div[1]/a/div/img')
    image_links5 = [img.get_attribute('src') for img in image_elements5]
    product_links5 = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[5]/div/div/div[1]/div[1]/a')
    product_urls5 = [img.get_attribute('href') for img in product_links5]

    print(NAME5)
    print(Price5)
    print(image_links5)
    print(product_urls5)
    print("")


def searchinfo():
    driver = webdriver.Chrome()
    driver.get(text2)
    '''
    driver.execute_script("document.body.style.zoom='50%'")

    show = driver.find_element(By.XPATH,' /html/body/div[4]/div/div[10]/div[1]/div[1]/div/div/div/div[2]/button')
    show.click()
    '''
    NAMEI1 = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div[2]/div/div[1]/div[3]/div/div/h1').text
    PriceI1 = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div[2]/div/div[1]/div[8]/div/div/span').text
    image_elementsI1 = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div[3]/div[1]/div/div/div[1]/div/img')
    image_linksI1 = [img.get_attribute('src') for img in image_elementsI1]
    image_elementsII2 = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div[10]/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/div[3]/div[5]/div/div/div/div/div/div/img')
    image_linksII2 = [img.get_attribute('src') for img in image_elementsII2]




    print(NAMEI1)
    print(PriceI1)
    print(image_linksI1)
    print(image_linksII2)
    print("")

    '''
    NAME1 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a').text
    Price1 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/span').text
    image_elements1 = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div[1]/a/div/img')
    image_links1 = [img.get_attribute('src') for img in image_elements1]
    product_links1 = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div[1]/a')
    product_urls1 = [img.get_attribute('href') for img in product_links1]
    
    print(NAME1)
    print(Price1)
    print(image_links1)
    print(product_urls1)
    print("")
    '''

    





Get1 = input("s:Search Item  ,  i:Item info  , e:exit = ")
print(Get1)
if Get1 == 's' :
    text1 = input("Search Item : ") 
    Searchitem ()
if Get1 == 'i' :
    text2 = input("Item info link : ") 
    searchinfo ()
if Get1 == 'e' :
    exit



