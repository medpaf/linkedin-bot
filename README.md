# Linkedin Bot
Automation bot for Linkedin. This script asks for new connections on the Linkedin platform. 

## Installation

The only external library used in this script is the Selenium framework. To install it run one of the following command on your system (you'll need to have pip3 installed on your machine).

On Linux, run:
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

After the installation, simply run the python file.

On Linux:
```
python3 linkedin-bot.py
```

On Windows and macOS:
```
python linkedin-bot.py
```

Disclaimer: Use this script with caution since Linkedin has a weekly limit of new connections and may block or flag your account.
