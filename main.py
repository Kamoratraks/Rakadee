from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from fastapi import FastAPI
from selenium.webdriver.chrome.options import Options
from flask import Flask, jsonify, request, render_template
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import  Request
from fastapi.responses import JSONResponse
app = Flask(__name__)

" ใช้ตัวนี้ run "
" uvicorn main:app --reload "

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/api/data")
async def root():
    # Convert myArray to JSON
    return json.dumps("myArray", ensure_ascii=False)
# @app.post('/sent_info')
# async def send_info(data: dict):
#     info_data = data.get('data')
#     global myArray2
#     chrome_options = Options()
#     chrome_options.add_argument("--window-size=80%,80%")
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get(info_data)
    
    
#     time.sleep(0.5)
#     driver.execute_script("document.body.style.zoom='20%'")
#     time.sleep(2)



    

#     NAMEI1 = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div[2]/div/div[1]/div[3]/div/div/h1').text
#     PriceI1 = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div[2]/div/div[1]/div[8]/div/div/span').text
#     image_elementsI1 = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div[3]/div[1]/div/div/div[1]/div/img')
#     image_linksI1 = [img.get_attribute('src') for img in image_elementsI1]
#     image_elementsII2 = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div[10]/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/div[3]/div[5]/div/div/div/div/div/div/img')
#     image_linksII2 = [img.get_attribute('src') for img in image_elementsII2]
#     info01 = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[10]/div[1]/div[1]/div/div/div').text
   





#     print(NAMEI1)
#     print(PriceI1)
#     print(image_linksI1)
#     print(image_linksII2)
#     print(info01)
#     print("")



#     myArray2 = [
#     {"NAMEI": [NAMEI1]},
#     {"PriceI": [PriceI1]},
#     {"image_linksI": [image_linksI1]},
#     {"image_linksII": [image_linksII2]},
#     {"info": [info01]}
#     ]
@app.post('/send_data')
async def receive_data(data: dict):
    received_data = data.get('data')
    print("Received data:", received_data)
    global myArray
   #driver = webdriver.Chrome()
    # driver.get('https://www.amazon.com/?&tag=googleglobalp-20&ref=pd_sl_7nnedyywlk_e&adgrpid=82342659060&hvpone=&hvptwo=&hvadid=393493755082&hvpos=&hvnetw=g&hvrand=10520968507142495629&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9073373&hvtargid=kwd-10573980&hydadcr=2246_11061421')
    # time.sleep(0.5)


    # s =driver.find_element(By.XPATH,' /html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
    # s.send_keys(received_data)
    # time.sleep(0.5)

    # s_click = driver.find_element(By.XPATH, value=' /html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
    # s_click.click()
    # time.sleep(0.5)
    # driver.execute_script("document.body.style.zoom='50%'")
    # time.sleep(2)

    # NAME_A1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2').text
    # Price_A1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a/span').text
    # image_elements_A1 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img')
    # image_links_A1 = [img.get_attribute('src') for img in image_elements_A1]
    # product_links_A1 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/span/a')
    # product_urls_A1 = [img.get_attribute('href') for img in product_links_A1]
    

    # print(NAME_A1)
    # print(Price_A1)
    # print(image_links_A1)
    # print(product_urls_A1)
    # print("")
    
    
    # NAME_A2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2').text
    # Price_A2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a/span').text
    # image_elements_A2 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img')
    # image_links_A2 = [img.get_attribute('src') for img in image_elements_A2]
    # product_links_A2 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/span/a')
    # product_urls_A2 = [img.get_attribute('href') for img in product_links_A2]

    # print(NAME_A2)
    # print(Price_A2)
    # print(image_links_A2)
    # print(product_urls_A2)
    # print("")

                                            
    # NAME_A3 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[2]/div/div/div[1]/h2').text
    # Price_A3 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/a/span/span[2]').text
    # image_elements_A3 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img')
    # image_links_A3 = [img.get_attribute('src') for img in image_elements_A3]
    # product_links_A3 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[1]/div/div[2]/div/span/a')
    # product_urls_A3 = [img.get_attribute('href') for img in product_links_A3]

    # print(NAME_A3)
    # print(Price_A3)
    # print(image_links_A3)
    # print(product_urls_A3)
    # print("")
   

    # NAME_A4 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div/div[2]/div/div/div[1]/h2').text
    # Price_A4 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/a/span/span[2]').text
    # image_elements_A4 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div')
    # image_links_A4 = [img.get_attribute('src') for img in image_elements_A4]
    # product_links_A4 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div/div[1]/div/div[2]/div/span/a')
    # product_urls_A4 = [img.get_attribute('href') for img in product_links_A4]
    
    # print(NAME_A4)
    # print(Price_A4)
    # print(image_links_A4)
    # print(product_urls_A4)
    # print("")

    # NAME_A5 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[9]/div/div/div/div/div/div[2]/div/div/div[1]/h2').text
    # Price_A5 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[9]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/a/span/span[2]').text
    # image_elements_A5 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[9]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img')
    # image_links_A5 = [img.get_attribute('src') for img in image_elements_A5]
    # product_links_A5 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[9]/div/div/div/div/div/div[1]/div/div[2]/div/span/a')
    # product_urls_A5 = [img.get_attribute('href') for img in product_links_A5]

    # print(NAME_A5)
    # print(Price_A5)
    # print(image_links_A5)
    # print(product_urls_A5)
    # print("")
    # print("=================================================================================================================================================")
    
    
    driver = webdriver.Chrome()
    driver.get('https://lazada.co.th')
    time.sleep(0.5)

    s =driver.find_element(By.XPATH,' /html/body/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/form/div/div[1]/input[1]')
    s.send_keys(received_data)
    time.sleep(0.5)

    s_click = driver.find_element(By.XPATH, value=' /html/body/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/form/div/div[2]/button')
    s_click.click()
    time.sleep(1)

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
    myArray = [
    {"Name": [NAME1, NAME2, NAME3,NAME4,NAME5]},
    {"Price": [Price1, Price2, Price3,Price4,Price5]},
    {"imglink": [image_links1,image_links2,image_links3,image_links4,image_links5]},
    {"product_urls": [product_urls1, product_urls2, product_urls3,product_urls4,product_urls5]}
    ]
    #product_urls_A1,product_urls_A2,product_urls_A3,product_urls_A4,product_urls_A5image_links_A1,image_links_A2,image_links_A3,image_links_A4,image_links_A5Price_A1,Price_A2,Price_A3,Price_A4,Price_A5,NAME_A1,NAME_A2,NAME_A3,NAME_A4,NAME_A5

    return {"EIEI myArray}
if __name__ == '__main__':
    app.run()


#def Searchitem ():
    # global myArray
    # driver = webdriver.Chrome()
    # driver.get('https://www.amazon.com/?&tag=googleglobalp-20&ref=pd_sl_7nnedyywlk_e&adgrpid=82342659060&hvpone=&hvptwo=&hvadid=393493755082&hvpos=&hvnetw=g&hvrand=10520968507142495629&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9073373&hvtargid=kwd-10573980&hydadcr=2246_11061421')
    # time.sleep(0.5)


    # s =driver.find_element(By.XPATH,' /html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
    # s.send_keys(text1)
    # time.sleep(0.5)

    # s_click = driver.find_element(By.XPATH, value=' /html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
    # s_click.click()
    # time.sleep(0.5)
    # driver.execute_script("document.body.style.zoom='50%'")
    # time.sleep(2)

    # NAME_A1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2').text
    # Price_A1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a/span').text
    # image_elements_A1 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img')
    # image_links_A1 = [img.get_attribute('src') for img in image_elements_A1]
    # product_links_A1 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/span/a')
    # product_urls_A1 = [img.get_attribute('href') for img in product_links_A1]
    

    # print(NAME_A1)
    # print(Price_A1)
    # print(image_links_A1)
    # print(product_urls_A1)
    # print("")
    
    
    # NAME_A2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2').text
    # Price_A2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a/span').text
    # image_elements_A2 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img')
    # image_links_A2 = [img.get_attribute('src') for img in image_elements_A2]
    # product_links_A2 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/span/a')
    # product_urls_A2 = [img.get_attribute('href') for img in product_links_A2]

    # print(NAME_A2)
    # print(Price_A2)
    # print(image_links_A2)
    # print(product_urls_A2)
    # print("")

                                            
    # NAME_A3 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[2]/div/div/div[1]/h2').text
    # Price_A3 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/a/span/span[2]').text
    # image_elements_A3 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img')
    # image_links_A3 = [img.get_attribute('src') for img in image_elements_A3]
    # product_links_A3 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[1]/div/div[2]/div/span/a')
    # product_urls_A3 = [img.get_attribute('href') for img in product_links_A3]

    # print(NAME_A3)
    # print(Price_A3)
    # print(image_links_A3)
    # print(product_urls_A3)
    # print("")
   

    # NAME_A4 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div/div[2]/div/div/div[1]/h2').text
    # Price_A4 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/a/span/span[2]').text
    # image_elements_A4 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div')
    # image_links_A4 = [img.get_attribute('src') for img in image_elements_A4]
    # product_links_A4 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div/div[1]/div/div[2]/div/span/a')
    # product_urls_A4 = [img.get_attribute('href') for img in product_links_A4]
    
    # print(NAME_A4)
    # print(Price_A4)
    # print(image_links_A4)
    # print(product_urls_A4)
    # print("")

    # NAME_A5 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[9]/div/div/div/div/div/div[2]/div/div/div[1]/h2').text
    # Price_A5 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[9]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/a/span/span[2]').text
    # image_elements_A5 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[9]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img')
    # image_links_A5 = [img.get_attribute('src') for img in image_elements_A5]
    # product_links_A5 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[9]/div/div/div/div/div/div[1]/div/div[2]/div/span/a')
    # product_urls_A5 = [img.get_attribute('href') for img in product_links_A5]

    # print(NAME_A5)
    # print(Price_A5)
    # print(image_links_A5)
    # print(product_urls_A5)
    # print("")
    # print("=================================================================================================================================================")
    

    # driver = webdriver.Chrome()
    # driver.get('https://lazada.co.th')
    # time.sleep(0.5)

    # s =driver.find_element(By.XPATH,' /html/body/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/form/div/div[1]/input[1]')
    # s.send_keys(text1)
    # time.sleep(0.5)

    # s_click = driver.find_element(By.XPATH, value=' /html/body/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/form/div/div[2]/button')
    # s_click.click()
    # time.sleep(1)

    # NAME1 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a').text
    # Price1 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/span').text
    # image_elements1 = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div[1]/a/div/img')
    # image_links1 = [img.get_attribute('src') for img in image_elements1]
    # product_links1 = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div[1]/a')
    # product_urls1 = [img.get_attribute('href') for img in product_links1]

    # print(NAME1)
    # print(Price1)
    # print(image_links1)
    # print(product_urls1)
    # print("")

    # NAME2 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/a').text
    # Price2 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div[3]/span').text
    # image_elements2 = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/a/div/img')
    # image_links2 = [img.get_attribute('src') for img in image_elements2]
    # product_links2 = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div[10]/div[1]/div[1]/div/div/div/div/div[1]/div')
    # product_urls2 = [img.get_attribute('href') for img in product_links2]

    # print(NAME2)
    # print(Price2)
    # print(image_links2)
    # print(product_urls2)
    # print("")

    # NAME3 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/a').text
    # Price3 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[3]/span').text
    # image_elements3 = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/a/div/img')
    # image_links3 = [img.get_attribute('src') for img in image_elements3]
    # product_links3 = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/a')
    # product_urls3 = [img.get_attribute('href') for img in product_links3]

    # print(NAME3)
    # print(Price3)
    # print(image_links3)
    # print(product_urls3)
    # print("")
   

    # NAME4 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[4]/div/div/div[2]/div[2]/a').text
    # Price4 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[4]/div/div/div[2]/div[3]/span').text
    # image_elements4 = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[4]/div/div/div[1]/div[1]/a/div/img')
    # image_links4 = [img.get_attribute('src') for img in image_elements4]
    # product_links4 = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[4]/div/div/div[1]/div[1]/a')
    # product_urls4 = [img.get_attribute('href') for img in product_links4]
    
    # print(NAME4)
    # print(Price4)
    # print(image_links4)
    # print(product_urls4)
    # print("")

    # NAME5 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[5]/div/div/div[2]/div[2]/a').text
    # Price5 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[5]/div/div/div[2]/div[3]/span').text
    # image_elements5 = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[5]/div/div/div[1]/div[1]/a/div/img')
    # image_links5 = [img.get_attribute('src') for img in image_elements5]
    # product_links5 = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[5]/div/div/div[1]/div[1]/a')
    # product_urls5 = [img.get_attribute('href') for img in product_links5]

    # print(NAME5)
    # print(Price5)
    # print(image_links5)
    # print(product_urls5)
    # print("")
    # myArray = [
    # {"Name": [NAME1, NAME2, NAME3,NAME4,NAME5,NAME_A1,NAME_A2,NAME_A3,NAME_A4,NAME_A5]},
    # {"Price": [Price1, Price2, Price3,Price4,Price5,Price_A1,Price_A2,Price_A3,Price_A4,Price_A5]},
    # {"imglink": [image_links1,image_links2,image_links3,image_links4,image_links5,image_links_A1,image_links_A2,image_links_A3,image_links_A4,image_links_A5]},
    # {"product_urls": [product_urls1, product_urls2, product_urls3,product_urls4,product_urls5,product_urls_A1,product_urls_A2,product_urls_A3,product_urls_A4,product_urls_A5]}
    # ]


# def searchinfo():
    # global myArray2
    # chrome_options = Options()
    # chrome_options.add_argument("--window-size=80%,80%")
    # driver = webdriver.Chrome(options=chrome_options)
    # driver.get(text2)
    
    
    # time.sleep(0.5)
    # driver.execute_script("document.body.style.zoom='20%'")
    # time.sleep(2)



    

    # NAMEI1 = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div[2]/div/div[1]/div[3]/div/div/h1').text
    # PriceI1 = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div[2]/div/div[1]/div[8]/div/div/span').text
    # image_elementsI1 = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div[3]/div[1]/div/div/div[1]/div/img')
    # image_linksI1 = [img.get_attribute('src') for img in image_elementsI1]
    # image_elementsII2 = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div[10]/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/div[3]/div[5]/div/div/div/div/div/div/img')
    # image_linksII2 = [img.get_attribute('src') for img in image_elementsII2]
    # info01 = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[10]/div[1]/div[1]/div/div/div').text
   





    # print(NAMEI1)
    # print(PriceI1)
    # print(image_linksI1)
    # print(image_linksII2)
    # print(info01)
    # print("")



    # myArray2 = [
    # {"NAMEI": [NAMEI1]},
    # {"PriceI": [PriceI1]},
    # {"image_linksI": [image_linksI1]},
    # {"image_linksII": [image_linksII2]},
    # {"info": [info01]}
    # ]
    
    
# def searchinfo_Amazon():
#     global myArray2
#     chrome_options = Options()
#     chrome_options.add_argument("--window-size=80%,80%")
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get(text2)
    
    
#     time.sleep(0.5)
#     driver.execute_script("document.body.style.zoom='20%'")
#     time.sleep(2)   

#     NAMEI1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[9]/div[5]/div[4]/div[1]/div/h1').text
#     PriceI1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[9]/div[5]/div[4]/div[13]/div[3]/div[1]/span[2]/span[1]').text
#     image_elementsI1 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[9]/div[5]/div[3]/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/ul/li[5]/span/span/div')
#     image_linksI1 = [img.get_attribute('src') for img in image_elementsI1]
#     image_elementsII2 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[9]/div[5]/div[3]/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/ul/li[5]/span/span/div/img')
#     image_linksII2 = [img.get_attribute('src') for img in image_elementsII2]
#     info01 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[9]/div[5]/div[4]/div[42]/div').text
   





#     print(NAMEI1)
#     print(PriceI1)
#     print(image_linksI1)
#     print(image_linksII2)
#     print(info01)
#     print("")



#     myArray2 = [
#     {"NAMEI": [NAMEI1]},
#     {"PriceI": [PriceI1]},
#     {"image_linksI": [image_linksI1]},
#     {"image_linksII": [image_linksII2]},
#     {"info": [info01]}
#     ]







# Get1 = input("s:Search Item  ,  i:Item info  , e:exit = ")
# print(Get1)
# if Get1 == 's' :
#     text1 = input("Search Item : ") 
#     Searchitem ()
# if Get1 == 'il' :
#     text2 = input("Item info link : ") 
#     searchinfo ()
# if Get1 == 'ia' :
#     text2 = input("Item info link : ") 
#     searchinfo_Amazon ()
# if Get1 == 'e' :
#     exit



