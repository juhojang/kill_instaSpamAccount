from cgitb import html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import UnexpectedAlertPresentException
import time


driver= webdriver.Edge(r"C:/msedgedriver.exe")
driver.implicitly_wait(3)
driver.get('https://www.instagram.com/login')
login_x_path='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button'
search_x_path='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[1]/div/div[2]/div[2]/div/a/div/div/div/div'
search_text_x_path='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input'
block_x_path='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/a/div'
setting_x_path='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[1]/div[2]/button'
block_button_x_path='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[1]'
real_block_x_path='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[1]'
cancel_x_path='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button'


print("id를 입력하세요.")
id=input()
print("password를 입력하세요.")
password=input()

try :
    driver.find_element('name','username').send_keys(id)
    driver.find_element('name','password').send_keys(password)
    driver.find_element('xpath',login_x_path).click()
except UnexpectedAlertPresentException:
    print("hi")
try:
    driver.find_element('xpath',login_x_path).click()
except :
    print("bye")


list=['','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for j in list:
    i=1
    while 1:
        time.sleep(3)
    
        try:
            driver.find_element('xpath',search_x_path).click()
            driver.find_element('xpath',search_text_x_path).send_keys("부업"+j)
        except:
            pass
    
        try:
            print('/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div['+str(i)+']/div/a/div')
            driver.find_element('xpath','/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div['+str(i)+']/div/a/div').click()
            time.sleep(3)
        except:
            try:
                driver.find_element('xpath',search_x_path).click()
                driver.find_element('xpath',search_text_x_path).send_keys("부업"+j)
                driver.find_element('xpath','/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div['+str(i)+']/div/a/div').click()
                time.sleep(3)
            except:
                print("there is no list")
                break
        try:
            driver.find_element('xpath',setting_x_path).click()
            driver.find_element('xpath',block_button_x_path).click()
            driver.find_element('xpath',real_block_x_path).click()
            success=driver.find_element('xpath','/html/body/div[4]/div[1]/div/div/div/p').text
            print(success)
            if success=='문제가 발생했습니다. 다시 시도해보세요.':
                print(success)
                print("sleep")
                time.sleep(300)
                driver.refresh()
            else:
                driver.refresh()
                time.sleep(3)

    
        except Exception as e:
            print("no setting button")
            i=i+1
    time.sleep(10)

