from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    from webdriver_manager.chrome import ChromeDriverManager
    browser = webdriver.Chrome(ChromeDriverManager().install())
		
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = WebDriverWait(browser, 12).until(
         EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    #button.click()
    message = browser.find_element_by_id("book")
    message.click()

    #assert "successful" in message.text
	
    x_elem = browser.find_element_by_css_selector("[id='input_value']")
    x = x_elem.text
    y = calc(x)
   
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
   
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()
   
finally:
   # успеваем скопировать код за 30 секунд
    time.sleep(60)
   # закрываем браузер после всех манипуляций
    browser.quit()