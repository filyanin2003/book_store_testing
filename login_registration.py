# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# try:
#     chop = webdriver.ChromeOptions()
#     chop.add_extension("C:/extension_5_3_3_0.crx") #установка расширения ad block
#     driver = webdriver.Chrome(chrome_options=chop)
#     driver.maximize_window()
#     driver.get(" http://practice.automationtesting.in/")
#     current_page = driver.current_url
#     driver.execute_script("window.open();")
#     window_after = driver.window_handles[2]
#     driver.switch_to.window(window_after)
#     driver.close()
#     window_after = driver.window_handles[1]
#     driver.switch_to.window(window_after)
#     driver.close()
#     window_after = driver.window_handles[0]
#     driver.switch_to.window(window_after)
#     driver.get(current_page)
#     driver.implicitly_wait(5)
#     my_account_menu = driver.find_element(By.LINK_TEXT, "My Account")
#     my_account_menu.click()
#     register_email = driver.find_element(By.ID, "reg_email")
#     register_email.send_keys("filyanin1992@mail.ru")
#     register_password = driver.find_element(By.ID, "reg_password")
#     register_password.send_keys("2003Password2023")
#     register_btn = driver.find_element(By.NAME, "register")
#     register_btn.click()
#
# finally:
#     driver.quit()

#Leave 1 line empty

#Login on site
from selenium import webdriver
from selenium.webdriver.common.by import By

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
    driver.close()
    window_after = driver.window_handles[0]
    driver.switch_to.window(window_after)
    driver.get(current_page)
    driver.implicitly_wait(5)
    my_account_menu = driver.find_element(By.LINK_TEXT, "My Account")
    my_account_menu.click()
    login_email = driver.find_element(By.ID, "username")
    login_email.send_keys("filyanin1992@mail.ru")
    login_password = driver.find_element(By.ID, "password")
    login_password.send_keys("2003Password2023")
    login_btn = driver.find_element(By.NAME, "login")
    login_btn.click()
    logout = driver.find_element(By.LINK_TEXT, "Logout")
    if logout is not None:
        print("There is an element on the page")
    else:
        print("The element is missing on the page")

finally:
    driver.quit()

#Leave 1 line empty