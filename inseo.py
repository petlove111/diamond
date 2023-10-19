
#driver2=webdriver.Chrome()

#driver1.get("https://www.naver.com")
#driver2.get("https://comic.naver.com/index")

#driver1.back()
#driver1.forward()
#driver1.close()

#driver1.maximize_window()
#driver1.minimize_window()
#driver1.set_window_size(500,300)
#driver1.set_window_position(100,100)

#u=["https://www.naver.com","https://www.youtube.com","https://comic.naver.com"]
#d=[]
#for i in range(len(u)):
#    driver=webdriver.Chrome()
#    d.append(driver)
#   d[i].get(u[i])
#import time

#driver1.set_window_size(200,300)
#driver1.set_window_position(0,0)
#for i in range(4):
#   time.sleep(1)
#   driver1.set_window_position(i*100, i*100)

'''
from selenium import webdriver

w=1920/2
h=1080/2

pos=[(0,0),(w,0),(0,h),(w,h)]

d=[]

u=["https://www.naver.com","https://www.youtube.com","https://comic.naver.com","https://github.com"]

for i in range(len(u)):
    driver=webdriver.Chrome()
    d.append(driver)
    d[i].set_window_size(w,h)
    d[i].set_window_position(pos[i][0],pos[i][1])
    d[i].get(u[i])


'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)

driver.get("https://gg.gg/webcrawling")

p='//*[@id="homePageLinks"]/ul/li/a'
e=driver.find_element('xpath',p)
e.click()

import time
time.sleep(2)







