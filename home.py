from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

try:
    chop = webdriver.ChromeOptions()
    chop.add_extension("C:/extension_5_3_3_0.crx") #установка расширения ad block
    driver = webdriver.Chrome(chrome_options=chop)
    driver.maximize_window()
    driver.get(" http://practice.automationtesting.in/")
    current_page = driver.current_url
    driver.execute_script("window.open();")
    window_after = driver.window_handles[2]
    driver.switch_to.window(window_after)
    driver.close()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    driver.get(current_page)
    driver.implicitly_wait(5)
    driver.execute_script("window.scrollBy(0, 600);")
    selenium_ruby_book = driver.find_element(By.CSS_SELECTOR, ".post-160 .attachment-shop_catalog")
    selenium_ruby_book.click()
    reviews_btn = driver.find_element(By.CSS_SELECTOR, ".reviews_tab>a")
    reviews_btn.click()
    star_5 = driver.find_element(By.CSS_SELECTOR, ".star-5")
    star_5.click()
    your_review = driver.find_element(By.ID, "comment")
    your_review.send_keys("Nice book!")
    name = driver.find_element(By.ID, "author")
    name.send_keys("Anton2003")
    email = driver.find_element(By.ID, "email")
    email.send_keys("anton2003@mail.ru")
    submit_btn = driver.find_element(By.ID, "submit")
    submit_btn.click()

finally:
    driver.quit()

#Leave 1 line empty