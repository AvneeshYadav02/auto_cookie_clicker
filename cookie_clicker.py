from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

WEBSITE = "https://ozh.github.io/cookieclicker/"

driver = webdriver.Firefox()
driver.get(WEBSITE)

sleep(5)

print("Selecting language...")
try:
    lang_select = driver.find_element(By.ID, "langSelect-EN" )
    lang_select.click()
    print("Selected English")
except NoSuchElementException:
    print("Lang not found!!!!")

big_cookie = driver.find_element(By.ID, "bigCookie")

sleep(5)

current_time = time()

while (True):
    big_cookie.click()

    #Every 5 seconds
    if (time() - current_time >= 3):
        # Buy products 
        item_no = 0
        highest_price = ("product_nil", 0)

        #Available Currency
        my_cookies = driver.find_element(By.ID, "cookies")
        my_cookies = my_cookies.text
        my_cookies = my_cookies.split(" ")[0]
        my_cookies = int(my_cookies.replace(",", ""))

        #List of all available items
        item_list = driver.find_elements(By.CLASS_NAME, "unlocked")


        if (len(item_list) != 0):
            for item in item_list:
                # Getting Item price and convert it into integer
                item = item.text.split("\n")
                item[1] = item[1].replace(',', '')

                product_tup = (f"product{item_no}", item[1])

                # If product is affordable and the most expensive 
                if (int(highest_price[1]) <= int(item[1]) and my_cookies >= int(item[1])):
                        highest_price = product_tup
                
                item_no += 1
 
            try:
                buy_prod = driver.find_element(By.ID, highest_price[0])
                buy_prod.click()
            except (NoSuchElementException):
                print("Nothing to buy")

        # Update the current time
        current_time = time()