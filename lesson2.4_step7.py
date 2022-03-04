from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
 

try:
	from webdriver_manager.chrome import ChromeDriverManager
	browser = webdriver.Chrome(ChromeDriverManager().install())
	# говорим WebDriver ждать все элементы в течение 5 секунд
	
	browser.get("http://suninjuly.github.io/wait2.html")
    
    button = browser.find_element_by_id("button")
	button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "verify"))
        )
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text
	
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(60)
    # закрываем браузер после всех манипуляций
    browser.quit()