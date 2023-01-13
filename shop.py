# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
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
#     login_email = driver.find_element(By.ID, "username")
#     login_email.send_keys("filyanin1992@mail.ru")
#     login_password = driver.find_element(By.ID, "password")
#     login_password.send_keys("2003Password2023")
#     login_btn = driver.find_element(By.NAME, "login")
#     login_btn.click()
#     shop_menu = driver.find_element(By.LINK_TEXT, "Shop")
#     shop_menu.click()
#     html5_forms_book = driver.find_element(By.CSS_SELECTOR, ".post-181 .wp-post-image")
#     html5_forms_book.click()
#     print(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".entry-title"))).text)
#
# finally:
#     driver.quit()

#Leave 1 line empty

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
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
#     login_email = driver.find_element(By.ID, "username")
#     login_email.send_keys("filyanin1992@mail.ru")
#     login_password = driver.find_element(By.ID, "password")
#     login_password.send_keys("2003Password2023")
#     login_btn = driver.find_element(By.NAME, "login")
#     login_btn.click()
#     shop_menu = driver.find_element(By.LINK_TEXT, "Shop")
#     shop_menu.click()
#     html_category = driver.find_element(By.LINK_TEXT, "HTML")
#     html_category.click()
#     product_count = driver.find_elements(By.CSS_SELECTOR, ".attachment-shop_catalog")
#     if len(product_count) == 3:
#         print("В категории HTML 3 товара")  # len здесь посчитает количество элементов, найденных при помощи find_elements
#     else:
#         print("Ошибка. Количество товаров в категории HTML: " + str(len(product_count)))
#
# finally:
#     driver.quit()
#
# #Leave 1 line empty



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.select import Select
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
#     login_email = driver.find_element(By.ID, "username")
#     login_email.send_keys("filyanin1992@mail.ru")
#     login_password = driver.find_element(By.ID, "password")
#     login_password.send_keys("2003Password2023")
#     login_btn = driver.find_element(By.NAME, "login")
#     login_btn.click()
#     shop_menu = driver.find_element(By.LINK_TEXT, "Shop")
#     shop_menu.click()
#     sorting = driver.find_element(By.NAME, "orderby")
#     select = Select(sorting)
#     select.select_by_value("menu_order")
#     print(select.select_by_value("menu_order"))
#     #print(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Default sorting"))).text)
#     select.select_by_value("price-desc")
#     sorting = driver.find_element(By.NAME, "orderby")
#     select = Select(sorting)
#     select.select_by_value("price-desc")
#     print(select)
#
# finally:
#     driver.quit()

#Leave 1 line empty

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.select import Select
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
#     login_email = driver.find_element(By.ID, "username")
#     login_email.send_keys("filyanin1992@mail.ru")
#     login_password = driver.find_element(By.ID, "password")
#     login_password.send_keys("2003Password2023")
#     login_btn = driver.find_element(By.NAME, "login")
#     login_btn.click()
#     shop_menu = driver.find_element(By.LINK_TEXT, "Shop")
#     shop_menu.click()
#     android_guide_book = driver.find_element(By.CSS_SELECTOR, ".post-169 .wp-post-image")
#     android_guide_book.click()
#     old_price = driver.find_element(By.CSS_SELECTOR, ".post-169 del .woocommerce-Price-amount")
#     old_price_text = old_price.text
#     print(old_price_text)
#     assert old_price_text == "₹600.00"
#     new_price = driver.find_element(By.CSS_SELECTOR, ".post-169 ins .woocommerce-Price-amount")
#     new_price_text = new_price.text
#     print(new_price_text)
#     assert new_price_text == "₹450.00"
#     # WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".wp-post-image")))
#     android_book_cover = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".size-shop_single")))
#     android_book_cover.click()
#     pp_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
#     pp_close.click()
#
# finally:
#     time.sleep(5)
#     driver.quit()

#Leave 1 line empty


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.select import Select
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
#     shop_menu = driver.find_element(By.LINK_TEXT, "Shop")
#     shop_menu.click()
#     add_to_basket_html5 = driver.find_element(By.CSS_SELECTOR, ".post-182 .button")
#     add_to_basket_html5.click()
#     item_count = driver.find_element(By.CSS_SELECTOR, ".cartcontents")
#     item_count_text = item_count.text
#     print(item_count_text)
#     assert item_count_text == "1 Item"
#     cost = driver.find_element(By.CSS_SELECTOR, ".wpmenucartli .amount")
#     cost_text = cost.text
#     print(cost_text)
#     assert cost_text == "₹180.00"
#     basket = driver.find_element(By.CSS_SELECTOR, ".wpmenucart-contents")
#     basket.click()
#     subtotal = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount"), "180.00"))
#     print(subtotal)
#     total = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount"), "183.60"))
#     print(total)
#
# finally:
#     time.sleep(5)
#     driver.quit()


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.select import Select
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
#     shop_menu = driver.find_element(By.LINK_TEXT, "Shop")
#     shop_menu.click()
#     driver.execute_script("window.scrollBy(0, 300);")
#     add_to_basket_html5 = driver.find_element(By.CSS_SELECTOR, ".post-182 .button")
#     add_to_basket_html5.click()
#     time.sleep(5)
#     add_to_basket_mastering_js = driver.find_element(By.CSS_SELECTOR, ".post-165 .button")
#     add_to_basket_mastering_js.click()
#     time.sleep(5)
#     basket = driver.find_element(By.CSS_SELECTOR, ".wpmenucartli i")
#     basket.click()
#     time.sleep(5)
#     delete_html5 = driver.find_element(By.CSS_SELECTOR, ".cart_item:nth-child(1) .remove")
#     delete_html5.click()
#     undo = driver.find_element(By.LINK_TEXT, "Undo?")
#     undo.click()
#     quantity_mastering_js = driver.find_element(By.CSS_SELECTOR, ".cart_item:nth-child(1) input")
#     quantity_mastering_js.clear()
#     quantity_mastering_js.send_keys(3)
#     update_basket = driver.find_element(By.NAME, "update_cart")
#     update_basket.click()
#     time.sleep(5)
#     quantity_mastering_js = driver.find_element(By.CSS_SELECTOR, ".cart_item:nth-child(1) .qty")
#     quantity_mastering_js_text = quantity_mastering_js.text
#     assert quantity_mastering_js_text == "3" #не получается решить
#     print(quantity_mastering_js_text)
#     apply_coupon_btn = driver.find_element(By.NAME, "apply_coupon")
#     time.sleep(5)
#     apply_coupon_btn.click()
#     enter_code = driver.find_element(By.CSS_SELECTOR, ".woocommerce-error li")
#     enter_code_text = enter_code.text
#     print(enter_code_text)
#
# finally:
#     driver.quit()


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

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
    shop_menu = driver.find_element(By.LINK_TEXT, "Shop")
    shop_menu.click()
    driver.execute_script("window.scrollBy(0, 300);")
    add_to_basket_html5 = driver.find_element(By.CSS_SELECTOR, ".post-182 .button")
    add_to_basket_html5.click()
    time.sleep(5)
    basket = driver.find_element(By.CSS_SELECTOR, ".wpmenucartli i")
    basket.click()
    proceed_to_checkout = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button")))
    proceed_to_checkout.click()
    first_name_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
    first_name_field.send_keys("Anton")
    last_name_field = driver.find_element(By.ID, "billing_last_name")
    last_name_field.send_keys("Filyanin")
    email_field = driver.find_element(By.ID, "billing_email")
    email_field.send_keys("filyanin1992@mail.ru")
    phone_field = driver.find_element(By.ID, "billing_phone")
    phone_field.send_keys("+12345678989")
    select_country_field = driver.find_element(By.CSS_SELECTOR, ".select2-choice")
    select_country_field.click()
    input_country = driver.find_element(By.ID, "s2id_autogen1_search")
    # input_country.click()
    input_country.send_keys("Russia")
    select_input_country = driver.find_element(By.ID, "select2-results-1")
    select_input_country.click()
    street_address = driver.find_element(By.ID, "billing_address_1")
    street_address.send_keys("Omskaya_street")
    apartment = driver.find_element(By.ID, "billing_address_2")
    apartment.send_keys(1)
    city = driver.find_element(By.ID, "billing_city")
    city.send_keys("Omsk")
    county = driver.find_element(By.ID, "billing_state")
    county.send_keys("Omskaya")
    postcode = driver.find_element(By.ID, "billing_postcode")
    postcode.send_keys("555-000")
    driver.execute_script("window.scrollBy(0, 600);")
    time.sleep(5)
    check_payments = driver.find_element(By.ID, "payment_method_cheque")
    check_payments.click()
    place_order_btn = driver.find_element(By.ID, "place_order")
    place_order_btn.click()
    thank_you_text = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
    print(thank_you_text)
    payment_method = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method strong"), "Check Payments"))
    # payment_method_text = payment_method.text
    print(payment_method)

finally:
    driver.quit()