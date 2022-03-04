from selenium import webdriver
import time

try:
	from webdriver_manager.chrome import ChromeDriverManager
	browser = webdriver.Chrome(ChromeDriverManager().install())
	# говорим WebDriver искать каждый элемент в течение 5 секунд
	browser.implicitly_wait(5)

	browser.get("http://suninjuly.github.io/cats.html")

	button = browser.find_element_by_id("button")
	button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(60)
    # закрываем браузер после всех манипуляций
    browser.quit()