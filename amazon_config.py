from selenium import webdriver

DIRECTORY = "reports"
NAME = "PS4"
CURRENCY = "₹"
MIN_PRICE = "10000"
MAX_PRICE = "30000"
FILTERS = {
    "min": MIN_PRICE,
    "max": MAX_PRICE
}
BASE_URL = "https://www.amazon.in/"


def get_chrome_web_driver(options):
    return webdriver.Chrome('./chromedriver', chrome_options=options)


def get_web_driver_options():
    return webdriver.ChromeOptions()


def set_ignore_certificate_error(options):
    options.add_argument("--ignore-certificate-errors")


def set_incognito(options):
    options.add_argument("--incognito")
