# Linkedin Bot
Automation bot for Linkedin. This script asks for new connections on the Linkedin platform. 

## Installation

The only external library used in this script is the Selenium framework. To install it run the following command on your system (you'll need to have pip3 installed on your machine):
```
sudo pip3 install selenium
```
On Windows, use the following command:
```
python -m pip install selenium
```
On macOS, type:
```
pip install selenium
```

You'll also need to install geckodriver for the browser you use. If you aren't using Firefox as your browser, don't forget to change the line `driver = webdriver.Firefox()` on the script and specify your browser.

## How to use

After that, simply run the python file:
```
python3 linkedin-bot.py
```
(on Linux systems)

Disclaimer: Use this script with caution since Linkedin has a weekly limit of new connections and may block or flag your account.
