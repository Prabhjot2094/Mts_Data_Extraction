from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
import time
import robot
from sms_2 import *



#driver = webdriver.PhantomJS()
driver = webdriver.Chrome('C:\Python27\selenium\webdriver\chromedriver')
driver.get('https://selfcare.mtsindia.in/index.html')

# robot.keyPress(KeyEvent.VK_ALT);  				
# robot.keyPress(KeyEvent.VK_TAB);  
# robot.keyRelease(KeyEvent.VK_TAB); 
# robot.keyRelease(KeyEvent.VK_ALT);

Number = driver.find_element_by_id('regno')
Number.send_keys('9560500385')

Password = driver.find_element_by_id('password')
Password.send_keys('psnapster')

Submit = driver.find_element_by_name('Submit')
Submit.send_keys(Keys.RETURN)

#time.sleep(5)
elem = driver.find_element_by_xpath("//ul[@id='fup_container']/ul[1]")
s1 = elem.text.encode('utf8')
elem = driver.find_element_by_xpath("//ul[@id='fup_container']/ul[2]")
s1 += elem.text.encode('utf8')

seccess = sendSMS(s1)

time.sleep(5)
driver.quit()