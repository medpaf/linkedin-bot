# Linkedin Bot
Automation bot for Linkedin. This script asks for new connections on the Linkedin platform. 
The only external library used in this script is the Selenium framework. To install it run the following command on your system:
```
sudo pip3 install selenium
```
You'll also need to install geckodriver for browser you use. If you aren't using Firefox as your browser, don't forget to change the line `driver = webdriver.Firefox()` on the script.
After that, simply run the python file:
```
python3 linkedin-bot.py
```
Disclaimer: Use this script with caution since Linkedin has a daily limit of new connections and may block or flag your account.
