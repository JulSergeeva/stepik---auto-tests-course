from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
from webdriver_manager.chrome import ChromeDriverManager 
browser = webdriver.Chrome(ChromeDriverManager().install())

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
	
	button = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
       )
	button1 = browser.find_element_by_css_selector(".btn.btn-primary")
    button1.click()
		
	def calc(x):
     return str(math.log(abs(12*math.sin(int(x)))))
	 
	x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
	
	element = browser.find_element_by_css_selector("#answer")
    element.send_keys(y)
	
	
	button=browser.find_element_by_css_selector("#solve")
	button.click()
	
	

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
