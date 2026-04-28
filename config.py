import os
from dotenv import load_dotenv

load_dotenv()

AMAZON_URL = "https://www.amazon.in"

SEARCH_QUERIES = {
    "iphone": "Apple iPhone 16 Pro 128GB",
    "galaxy": "Samsung Galaxy S25 Ultra 256GB",
}

BROWSER           = os.getenv("BROWSER", "chrome")
HEADLESS          = os.getenv("HEADLESS", "false").lower() == "true"
IMPLICIT_WAIT     = 8
PAGE_LOAD_TIMEOUT = 30
EXPLICIT_WAIT     = 15

LT_USERNAME   = os.getenv("LT_USERNAME", "")
LT_ACCESS_KEY = os.getenv("LT_ACCESS_KEY", "")
LT_HUB_URL    = f"https://{LT_USERNAME}:{LT_ACCESS_KEY}@hub.lambdatest.com/wd/hub"

LT_CAPABILITIES = {
    "browserName"    : "Chrome",
    "browserVersion" : "latest",
    "LT:Options"     : {
        "platform"        : "Windows 11",
        "build"           : "Amazon Product Search - Selenium",
        "project"         : "Amazon Automation Assignment",
        "name"            : "iPhone & Galaxy Cart Tests",
        "selenium_version": "4.0.0",
        "w3c"             : True,
        "video"           : True,
        "network"         : True,
        "console"         : True,
        "visual"          : True,
        "tunnel"          : False,
    },
}

BASE_DIR       = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")
REPORT_DIR     = os.path.join(BASE_DIR, "reports")