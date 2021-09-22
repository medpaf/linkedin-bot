import sys
from selenium import webdriver

driver = webdriver.Firefox()

# Log in

site = 'https://www.linkedin.com'
driver.get(site)
driver.implicitly_wait(3)

username_field = driver.find_element_by_xpath("//input[@name='session_key']")
password_field = driver.find_element_by_xpath("//input[@name='session_password']")

username = 'paulofernandesmedeiros@gmail.com'
password = 'Fernandes1997'

username_field.send_keys(username)
password_field.send_keys(password)
driver.implicitly_wait(2)

submit_button = driver.find_element_by_xpath("//button[@type='submit']")
submit_button.click()

# Add contacts

start_page = 1
site_contacts = f'https://www.linkedin.com/search/results/people/?origin=SWITCH_SEARCH_VERTICAL&page={start_page}&sid=5Zt'

pages = int(input('How many pages?: '))

if pages > 10:
    print('You should not do that many pages. Linkedin may block or flag you. Try a smaller number next time')
    driver.close()
    sys.exit('Program ended.')

try:

    driver.get(site_contacts)
    driver.implicitly_wait(2)

    for i in range(0, pages):
        site_contacts = site_contacts = f'https://www.linkedin.com/search/results/people/?origin=SWITCH_SEARCH_VERTICAL&page={i+1}&sid=5Zt'
        driver.get(site_contacts)
        print(f'Page number: {i+1}')
        all_buttons = driver.find_elements_by_tag_name("button")
        connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]
        print(f'Connect buttons: {len(connect_buttons)}') 
        
        for btn in connect_buttons:
            driver.execute_script("arguments[0].click();", btn)
            driver.implicitly_wait(5)
            send = driver.find_element_by_xpath("//button[@aria-label='Send now']")
            driver.execute_script("arguments[0].click();", send)
            close = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
            driver.execute_script("arguments[0].click();", close)
            driver.implicitly_wait(5)
            
except KeyboardInterrupt():
    print('Operation was cancelled')
    driver.close()
    sys.exit()
except error as e:
    print(e)
else:
    print('Operation was succesfull.')
            




