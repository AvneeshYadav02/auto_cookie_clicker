# **COOKIE CLICKER AUTOMATOR**

A **Python** automation script that uses Selenium to play [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/). The bot automatically clicks the big cookie, handles language selection and automatically purchases the most expensive & purchasable item from the in-game shop.

![cookie-clicker](./gif/cookie_click.gif)

# *PREREQUISITES*
Before running the script please make sure that you have the Firefox browser and the Selenium library installed.

# *USAGE*
1. Clone this repository:
   ```bash
   git clone https://github.com/AvneeshYadav02/auto_cookie_clicker
   ```
2. Install dependencies:
   ```bash
   pip install selenium
   ```
3. Run the script:
    ```bash
    python3 cookie_clicker.py
    ```

# *WORKING*
The script works as per the following logic:

1. The script first opens the firefox browser and selects the language (English).

2. Clicks on the big cookie continuously

3. Every three seconds:
    1. Gets the amount of cookies available.
    
    2. Gets the available products in the shop (not upgrades). 
    
    3. Purchases the most expensive Product from the list of available products.

4.  Loops infinitely
